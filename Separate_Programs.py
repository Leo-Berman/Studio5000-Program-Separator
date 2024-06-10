import User_Interactions as UI
import File_IO as FIO
import Data_Processing as DP
def main():

    # Tell the user to select an L5K file
    UI.prompt("Please select an L5K file to process","L5K Selector",Verbose = False)

    # Have the user select an L5K file
    input_filepath = UI.prompt_input_filepath(Verbose = False)

    # Load the file into memory
    to_process = FIO.load_file(input_filepath,Verbose = False)


    # Tell the user to select a folder
    UI.prompt("Please select an output folder","Output File Path Prompt")

    # Get the output folder
    output_filepath = UI.prompt_output_filepath(Verbose = False)

    # Separate and Write the files
    DP.separate(output_filepath,to_process,Verbose=False)
if __name__ == "__main__":
    main()
