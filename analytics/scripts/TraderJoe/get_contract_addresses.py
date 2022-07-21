from duneanalytics import DuneAnalytics
import pickle, os

def get_data(uname, pwd, query_id, fname):
    dune = DuneAnalytics(uname, pwd)
    dune.login()
    dune.fetch_auth_token()

    result_id = dune.query_result_id(query_id=query_id)
    data = dune.query_result(result_id)

    write_data(data, fname)

    return data

def write_data(data, fname):
    pickle.dump(data, open(fname,'wb'))
    print(f'Data of type {type(data)} and length {len(data)} written to {fname}')

def read_data(fname):
    return pickle.load(open(fname,'rb'))

if __name__ == '__main__':
    fname = 'data.p'
    if fname in os.listdir():
        data = read_data(fname)
    else:
        uname = input('Dune Username?\n')
        pwd = input('Dune Password?\n')
        query_id = ''
        while isinstance(query_id, str):
            query_id = input('Query ID?\n')
            try:
                query_id = int(query_id)
            except:
                pass
        data = get_data(uname, pwd, query_id, fname)