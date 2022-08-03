from pathlib import Path
import api,coh,overheads,profit_loss,re



def main():

    forex=api.api_function()
    overheads.overhead_function(forex)
    coh.coh_function(forex)
    profit_loss.profitloss_function(forex)
    
main()
    