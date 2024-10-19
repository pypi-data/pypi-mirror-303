"""Main utility code."""

##############################################################################
# Allow future magic.
from __future__ import annotations

##############################################################################
# Python imports.
from argparse import ArgumentParser, Namespace
from datetime import datetime
from pathlib import Path
from typing import Final, NamedTuple

##############################################################################
# Markdownift imports.
from bs4.element import Tag
from markdownify import MarkdownConverter  # type: ignore

##############################################################################
# Timezime help.
from pytz import timezone


##############################################################################
def clean_img_name(image: Path) -> Path:
    """Clean up the name of an image.

    Args:
        image: The name of the image.

    Returns:
        The cleaned name of the image.

    Notes:
        Evernote sometimes has an image with no extension, called
        `Evernote`. I suspect this came about when an image was pasted in,
        or shared into the application in some way. This code ensures there
        is an extension.

        In every instance in my files it's always been a PNG.
    """
    return image if image.suffix else image.with_suffix(".png")


##############################################################################
class EvernoteConverter(MarkdownConverter):  # type: ignore
    """Markdownify class for pulling data out of Evernote HTML files."""

    def __init__(self) -> None:
        """Initialise the object."""
        super().__init__()
        self.found_title = ""
        self.found_tags: set[str] = set()
        self.time_created = ""
        self.time_updated = ""
        self.latitide = ""
        self.longitude = ""
        self.altitude = ""
        self.photos: list[str] = []

    def convert_meta(self, el: Tag, text: str, convert_as_inline: bool) -> str:
        """Handle meta tags."""
        del text, convert_as_inline
        if not isinstance(item_property := el.get("itemprop"), str) or not isinstance(
            content := el.get("content"), str
        ):
            return ""
        if item_property == "tag":
            self.found_tags.add(content)
        elif item_property == "title":
            self.found_title = content
        elif item_property == "created":
            self.time_created = content
        elif item_property == "updated":
            self.time_updated = content
        elif item_property == "latitude":
            self.latitide = content
        elif item_property == "longitude":
            self.longitude = content
        elif item_property == "altitude":
            self.altitude = content
        return ""

    def convert_h1(self, el: Tag, text: str, convert_as_inline: bool) -> str:
        """Handle h1 tags."""
        del convert_as_inline
        try:
            if "noteTitle" in el["class"]:
                return f"## {text.strip()}\n\n"
        except KeyError:
            pass
        return ""

    def convert_div(self, el: Tag, text: str, convert_as_inline: bool) -> str:
        """Handle div tags."""
        del convert_as_inline
        try:
            if "para" in el["class"]:
                return f"{text.strip()}\n"
        except KeyError:
            pass
        return ""

    def convert_img(self, el: Tag, text: str, convert_as_inline: bool) -> str:
        """Handle img tags."""
        try:
            if isinstance(photo := el["src"], str):
                self.photos += [photo]
                return f"![[{clean_img_name(Path(photo)).name}]]"
        except KeyError:
            pass
        return str(super().convert_img(el, text, convert_as_inline))


##############################################################################
TIMEZONE: Final[str] = "Europe/London"
"""The timezone to use when presenting times."""


##############################################################################
class EvernoteEntry(NamedTuple):
    """Holds all the details of a journal entry in Evernote."""

    title: str
    """The title for the journal entry."""
    text: str
    """The text of the journal entry."""
    tags: set[str]
    """The tags for the journal entry."""
    time_created: datetime
    """The time the journal entry was created."""
    time_updated: datetime
    """The time the journal entry was last updated."""
    latitude: float | None
    """The latitude of the journal entry."""
    longitude: float | None
    """The longitude of the journal entry."""
    altitude: float | None
    """The altitude of the journal entry."""
    photos: list[str]
    """The list of photos associated with the journal entry."""

    @classmethod
    def from_html(cls, html: str) -> EvernoteEntry:
        """Create the Evernote entry from some HTML.

        Args:
            html: The HTML that contains the Evernote journal entry.

        Returns:
            A populated `EvernoteEntry` instance.
        """
        data_parser = EvernoteConverter()
        markdown = data_parser.convert(html).strip()
        return cls(
            data_parser.found_title,
            markdown,
            data_parser.found_tags,
            datetime.strptime(data_parser.time_created, "%Y%m%dT%H%M%S%z").astimezone(
                timezone(TIMEZONE)
            ),
            datetime.strptime(data_parser.time_updated, "%Y%m%dT%H%M%S%z").astimezone(
                timezone(TIMEZONE)
            ),
            float(data_parser.latitide) if data_parser.latitide else None,
            float(data_parser.longitude) if data_parser.longitude else None,
            float(data_parser.altitude) if data_parser.altitude else None,
            data_parser.photos,
        )

    @property
    def markdown_directory(self) -> Path:
        """The directory that this entry should be created in."""
        return Path(self.time_created.strftime("%Y/%m/%d/"))

    @property
    def markdown_attachment_directory(self) -> Path:
        """The location of the attachment directory associated with this journal entry."""
        return self.markdown_directory / "attachments"

    @property
    def markdown_file(self) -> Path:
        """The path to the Markdown file that should be made for this journal."""
        return self.markdown_directory / Path(
            self.time_created.strftime("%Y-%m-%d-%H-%M-%S-%f-%Z.md")
        )

    @property
    def _front_matter_tags(self) -> str:
        """The tags formatted for use in Markdown front matter."""

        def clean(tag: str) -> str:
            # TODO: Make the tag conversion configurable.
            return {"sl": "secondlife"}.get(tag, tag).replace(" ", "-").replace("&", "")

        return (
            f"tags:\n  - {'\n  - '.join(clean(tag) for tag in self.tags)}"
            if self.tags
            else ""
        )

    @property
    def markdown(self) -> str:
        """The Evernote journal entry as a markdown document."""

        # Start with the front matter.
        front_matter = "\n".join(
            matter
            for matter in (
                f"journal-time: {self.time_created}",
                f"modified-time: {self.time_updated}",
                f"timezone: {TIMEZONE}",
                f"latitude: {self.latitude}" if self.latitude is not None else "",
                f"longitude: {self.longitude}" if self.longitude is not None else "",
                f"altitude: {self.altitude}" if self.altitude is not None else "",
                f"photo-count: {len(self.photos)}",
                self._front_matter_tags,
                "original-type: html",
            )
            if matter
        )
        return (
            f"---\n{front_matter}\n---\n\n"
            f"# {self.time_created.strftime('%A, %-d %B %Y at %X')}\n\n{self.text}"
        )


##############################################################################
def get_args() -> Namespace:
    """Get the command line arguments.

    Returns:
        The command line arguments.
    """
    parser = ArgumentParser(
        prog="evernote2md",
        description="A tool for converting an Evernote export file into a daily-note Markdown collection",
    )

    parser.add_argument(
        "evernote_files",
        help="The directory that contains the unzipped Evernote export",
    )
    parser.add_argument(
        "target_directory",
        help="The directory where the Markdown files will be created",
    )

    return parser.parse_args()


##############################################################################
def export(evernote: Path, daily: Path) -> None:
    """Export the Evernote files to Markdown-based daily notes.

    Args:
        evernote: The source Evernote location.
        daily: The target daily location.
    """
    for source in evernote.glob("*.html"):
        if source.name != "Evernote_index.html":
            # Get the entry from the Evernote export.
            entry = EvernoteEntry.from_html(source.read_text())
            # Figure out the path to the output file.
            markdown = daily / entry.markdown_file
            # Ensure its directory exists so we can actually write the file.
            markdown.parent.mkdir(parents=True, exist_ok=True)
            markdown.write_text(entry.markdown)
            print(f"Exported {entry.time_created}")
            # If the entry has photos too...
            if entry.photos:
                # ...copy them to the attachment directory.
                (attachments := (daily / entry.markdown_attachment_directory)).mkdir(
                    parents=True, exist_ok=True
                )
                for photo in entry.photos:
                    print(f"\tAttaching {photo}")
                    (attachments / clean_img_name(Path(photo)).name).write_bytes(
                        (evernote / photo).read_bytes()
                    )


##############################################################################
def main() -> None:
    """Main entry point for the utility."""
    arguments = get_args()
    if not (evernote := Path(arguments.evernote_files)).is_dir():
        print("Evernote source needs to be a directory")
        exit(1)
    if not (daily := Path(arguments.target_directory)).is_dir():
        print("The target needs to be an existing directory")
        exit(1)
    export(evernote, daily)


##############################################################################
if __name__ == "__main__":
    main()

### __main__.py ends here
