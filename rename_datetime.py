import datetime
import sys,os,glob,shutil,subprocess
import argparse

def main(res):
    foldername = res['folder_name']
    time = datetime.datetime.now()
    outname = time.strftime(res['nameformat'])
    cmd = f'mv {foldername} {outname}'
    print(cmd)
    os.system(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('folder_name')
    parser.add_argument('--runtype',type=str,default=None)
    parser.add_argument('--nameformat',type=str,default=None)
    res = parser.parse_args()
    res = vars(res)

    default_strftime = '_%Y-%m-%d_%H%M%S'
    if res['runtype'] == None:
        res['runtype'] = ''
    else:
        res['runtype'] = '_'+res['runtype']
    if res['nameformat'] == None:
        res['nameformat'] = f'output{res["runtype"]}{default_strftime}'
    main(res)