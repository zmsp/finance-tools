import pandas as pd
import argparse



parser = argparse.ArgumentParser(description='Process Merrel Edge security csv export for yahoo finance')
parser.add_argument('input_file', metavar='f', type=str,
                    help='a file for processing')

parser.add_argument('--output', metavar='o', type=str, default="export.csv",required=False,
                    help="output file name")
args = parser.parse_args()

df =pd.read_csv(args.input_file)
yahoo_export =pd.DataFrame(columns=['Symbol', 'Current Price', 'Date', 'Time', 'Change', 'Open', 'High',
 'Low', 'Volume', 'Trade Date', 'Purchase Price', 'Quantity',
 'Commission', 'High Limit', 'Low Limit', 'Comment'])
yahoo_export[['Symbol', "Quantity", "Purchase Price", "Trade Date" ]] = df[["Symbol", "Quantity", "Unit Cost ($)", "Acquisition Date"]]
yahoo_export["Trade Date" ] = pd.to_datetime(df["Acquisition Date"], errors='coerce').dt.strftime('%Y%m%d')
yahoo_export["Comment"] = df['Account Registration'] + "-" + df['Account #'] + ","+df['Short/Long']
yahoo_export.to_csv(args.output, sep=',', index=False)
print("exported {} rows".format(yahoo_export.shape[0]))