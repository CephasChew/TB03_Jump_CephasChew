from pathlib import Path
import api,coh,overheads,profit_loss

def main():
  
    forex=api.api_function()
    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)
    

file_path = Path.cwd()/"CSV_reports"/"summary_report.txt"
file_path.touch()
print(file_path.exists())