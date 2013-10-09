
def main():
    data_list = get_data_list()
    monthly_averages = get_monthly_averages(data_list)
    get_print(monthly_averages)

def get_data_list():
    file_name = 'table.csv'
    data_file = open(file_name, 'r')
    data_list = []
    for line_str in data_file:
        data_list.append(line_str.strip().split(','))
    
    return data_list

def get_monthly_averages(data_list):
    monthly_averages = []
    month = None
    year = None
    num = 0
    den = 0
    for datum in data_list[1:]:
        y, m, d = datum[0].split('-')
        if m != month:
            if month is not None:
                avg = num / den
                monthly_averages.append((avg, '{}-{}'.format(year, month)))
                num = 0
                den = 0
            year = y
            month = m
        volume = int(datum[5])
        adjusted_close = float(datum[6])
        num += volume * adjusted_close
        den += volume
    
    return monthly_averages

def get_print(monthly_averages):
    monthly_averages.sort(reverse=True)
    six_best = monthly_averages[:6]
    six_worst = monthly_averages[-7:-1] 
    print('Six best')
    for datum in six_best:
        print(datum)
    print('Six worst')
    for datum in six_worst:
        print(datum)

                   

if __name__ == '__main__':
    main() 


