import pandas as pd
import os

def import_and_combine_excel_sheets(input_file_path, output_file_path):
    # Read all sheets from the Excel file
    excel_file = pd.ExcelFile(input_file_path)
    
    # Combine all sheets into a single DataFrame
    combined_df = pd.concat([pd.read_excel(excel_file, sheet_name=sheet) for sheet in excel_file.sheet_names], ignore_index=True)
    
    # Delete existing output file if it exists
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Existing file '{output_file_path}' has been deleted.")
    
    # Export the combined dataframe to a new Excel file
    combined_df.to_excel(output_file_path, index=False, sheet_name='Combined')
    
    print(f"All sheets from {input_file_path} have been combined and exported to {output_file_path}")
    print(combined_df.head())
    return combined_df

if __name__ == "__main__":
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the input file path (assuming it's in the same directory)
    input_file_path = os.path.join(current_dir, "my_custom_file.xlsx")
    
    # Set the output file path in the same directory
    output_file_path = os.path.join(current_dir, "my_combined_output.xlsx")
    
    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: Input file '{input_file_path}' not found.")
    else:
        import_and_combine_excel_sheets(input_file_path, output_file_path)