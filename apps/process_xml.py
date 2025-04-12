import os
import xml.etree.ElementTree as ET
import logging
import sys
import argparse
from rich.console import Console
from rich.panel import Panel

# --- Configuration (Relative to project root where script is run) ---
SOURCE_DATA_DIR = "Data"  # Original XML files directory
OUTPUT_DATA_DIR = os.path.join(SOURCE_DATA_DIR, "modified") # Modified XML files directory
LOG_DIR = "logs" # Log directory
LOG_FILE = os.path.join(LOG_DIR, "process.log")
DEFAULT_SUFFIX = "000"

# Initialize Rich Console
console = Console()

# --- Core Processing Logic ---
def setup_logging():
    """Sets up logging configuration."""
    os.makedirs(LOG_DIR, exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    # Add a handler to also print errors to console
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)

def process_xml_files(source_dir: str, output_dir: str, suffix: str):
    """Reads XML files, modifies JVNUMBER, and saves them.

    Args:
        source_dir: Path to the directory containing original XML files.
        output_dir: Path to the directory to save modified XML files.
        suffix: The string to append to the JVNUMBER text.
    """
    console.print(f"\nProcessing files in '[cyan]{source_dir}[/cyan]' with suffix '[yellow]{suffix}[/yellow]'...")
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(source_dir):
        logging.error(f"Source directory '{source_dir}' not found!")
        console.print(f"[bold red]Error:[/bold red] Source directory '{source_dir}' not found!")
        return

    processed_count = 0
    error_count = 0
    found_files = False

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".xml"):
            found_files = True
            file_path = os.path.join(source_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                modified = False

                for jvnumber in root.findall(".//JVNUMBER"):
                    if jvnumber.text:
                        # Ensure we don't add suffix multiple times if run again
                        if not jvnumber.text.endswith(suffix):
                            jvnumber.text += suffix
                            modified = True
                    else:
                        logging.warning(f"JVNUMBER tag found but empty in {filename}")

                if modified:
                    tree.write(output_path, encoding="utf-8", xml_declaration=True)
                    logging.info(f"Successfully processed and modified {filename} -> {output_path}")
                    console.print(f"[green]MODIFIED:[/green] {filename} -> {os.path.relpath(output_path)}")
                    processed_count += 1
                else:
                     # If no modification needed, optionally copy or just log
                    logging.info(f"No modification needed for {filename}. Skipped saving.")
                    console.print(f"[yellow]SKIPPED:[/yellow]  {filename} (no changes needed or already processed)")

            except ET.ParseError as e:
                logging.error(f"Error parsing XML {filename}: {e}")
                console.print(f"[bold red]XML Parse Error:[/bold red] {filename} - {e}")
                error_count += 1
            except Exception as e:
                logging.error(f"General error processing {filename}: {e}")
                console.print(f"[bold red]Error:[/bold red] Processing {filename} - {e}")
                error_count += 1

    if not found_files:
        console.print(f"[yellow]No .xml files found in '{source_dir}'.[/yellow]")
        logging.warning(f"No .xml files found in '{source_dir}'.")
    else:
        console.print(f"\n[bold]Processing Summary:[/bold]")
        console.print(f"  - Files Modified: [green]{processed_count}[/green]")
        console.print(f"  - Files with Errors: [red]{error_count}[/red]")
        console.print(f"  - Modified files saved in: '[cyan]{output_dir}[/cyan]'" )
        console.print(f"  - Check '[cyan]{LOG_FILE}[/cyan]' for detailed logs.")

# --- Main Execution --- 
if __name__ == "__main__":
    # Setup argparse
    parser = argparse.ArgumentParser(description="Modify JVNUMBER in XML files by adding a suffix.")
    parser.add_argument(
        "--suffix",
        type=str,
        default=DEFAULT_SUFFIX,
        help=f"The suffix to add to JVNUMBER. Defaults to '{DEFAULT_SUFFIX}'."
    )
    parser.add_argument(
        "--source",
        type=str,
        default=SOURCE_DATA_DIR,
        help=f"Directory containing the original XML files. Defaults to '{SOURCE_DATA_DIR}'."
    )
    parser.add_argument(
        "--output",
        type=str,
        default=OUTPUT_DATA_DIR,
        help=f"Directory to save the modified XML files. Defaults to '{OUTPUT_DATA_DIR}'."
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging()
    logging.info(f"Application started with args: suffix='{args.suffix}', source='{args.source}', output='{args.output}'")
    console.print(Panel(f"XML JVNUMBER Modifier - Suffix: '[yellow]{args.suffix}[/yellow]'", title="Task", expand=False))

    # Run the processing function with arguments
    process_xml_files(args.source, args.output, args.suffix)

    logging.info("Application finished.")
    console.print("\n[bold green]Processing complete.[/bold green]")
