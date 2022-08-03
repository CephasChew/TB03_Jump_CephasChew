from pathlib import Path
import api,coh,overheads,profit_loss

# create a file path for summary_report.txt
file_path = Path.cwd()/"CSV_reports"/"summary_report.txt"
#create a text file "summary_report" in the file path
file_path.touch()
# check to see if summary_report.txt was made successfully in the file path
print(file_path.exists())


def overhead_function(forex):
    





def main():
    forex=api.api_function()
    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)
main()
    