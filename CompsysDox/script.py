import os
import re
from docx import Document
from pathlib import Path

def process_word_file(file_path):
    """
    Process a Word file to remove timestamps and extra line breaks
    """
    try:
        # Load the document
        doc = Document(file_path)
        
        # Extract all text from paragraphs
        paragraphs = []
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if text:  # Only process non-empty paragraphs
                paragraphs.append(text)
        
        # Process the text
        processed_lines = []
        
        for line in paragraphs:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check if line starts with numbers (timestamp pattern)
            # This looks for lines that start with digits, possibly followed by colons, spaces, or other timestamp characters
            timestamp_pattern = r'^\d+[:\.\s\-]*\d*[:\.\s\-]*\d*'
            
            # If the line starts with a timestamp pattern and doesn't contain much text after it, skip it
            if re.match(timestamp_pattern, line):
                # Check if it's likely just a timestamp (short line, mostly numbers and time separators)
                # Allow lines that have substantial text after the numbers
                clean_line = re.sub(timestamp_pattern, '', line).strip()
                if len(clean_line) < 10:  # If remaining text is very short, likely just a timestamp
                    continue
                else:
                    # Keep the line but remove the timestamp part
                    line = clean_line
            
            # Add the processed line
            if line:  # Only add non-empty lines
                processed_lines.append(line)
        
        # Join sentences properly with spaces
        processed_text = ' '.join(processed_lines)
        
        # Clean up multiple spaces
        processed_text = re.sub(r'\s+', ' ', processed_text)
        
        return processed_text.strip()
        
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return None

def process_folder(folder_path, output_folder=None):
    """
    Process all Word files in a folder
    """
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        print(f"Folder {folder_path} does not exist!")
        return
    
    # Set output folder
    if output_folder is None:
        output_folder = folder_path / "processed"
    else:
        output_folder = Path(output_folder)
    
    # Create output folder if it doesn't exist
    output_folder.mkdir(exist_ok=True)
    
    # Find all Word files
    word_files = list(folder_path.glob("*.docx")) + list(folder_path.glob("*.doc"))
    
    if not word_files:
        print("No Word files found in the specified folder!")
        return
    
    print(f"Found {len(word_files)} Word file(s) to process...")
    
    for file_path in word_files:
        print(f"Processing: {file_path.name}")
        
        # Process the file
        processed_text = process_word_file(file_path)
        
        if processed_text:
            # Create output file path
            output_file = output_folder / f"{file_path.stem}_processed.txt"
            
            # Write processed text to file
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(processed_text)
                print(f"Saved: {output_file.name}")
            except Exception as e:
                print(f"Error saving {output_file}: {str(e)}")
        else:
            print(f"Failed to process: {file_path.name}")
    
    print(f"\nProcessing complete! Check the '{output_folder.name}' folder for results.")

def main():
    # Get folder path from user
    folder_path = input("Enter the path to the folder containing Word files: ").strip()
    
    # Remove quotes if present
    folder_path = folder_path.strip('"\'')
    
    # Optional: specify output folder
    output_choice = input("Enter output folder path (or press Enter for default 'processed' folder): ").strip()
    output_folder = output_choice.strip('"\'') if output_choice else None
    
    # Process the folder
    process_folder(folder_path, output_folder)

if __name__ == "__main__":
    # You can also run it directly by specifying the folder path here:
    process_folder(r"./")
    
    main()