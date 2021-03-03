import scrape
import process
import argparse
def FindJobs(jobTitle : str, jobType :str):
    url = scrape.get_url(base_url, jobTitle,jobType)
    df = scrape.get_offers(base_url,url)
    df_pr = process.process_offers(df,r'Data')
    df_pr.to_csv('offers.csv')
    return df_pr
if __name__ == "__main__":
    parser = argparse.ArgumentParser('Find a job offer' )
    parser.add_argument('-j','--job',help = "The job you are looking for", type=str, default= 'data')
    parser.add_argument('-t','--type',help = "Type of contract", type=str, default= 'internship')
    args = parser.parse_args()
    base_url = "https://www.indeed.fr"
    job = args.job
    jt = args.type
    df_pr = FindJobs(jobTitle = job, jobType = jt)
    print(len(df_pr))