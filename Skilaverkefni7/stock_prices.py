def get_file():
    file_name = input("Enter filename: ")
    return file_name


def get_data_list(file_name):
    try:
        data_file = open(file_name, "r")
        data_list = [ ] # start with an empty list
        for line_str in data_file:
            # strip end-of-line, split on commas, and append items to list
            data_list.append(line_str.strip().split(','))
        return data_list
    except FileNotFoundError:
        print("Filename {} not found!".format(file_name))
        return False


def get_monthly_averages(data_list):
    '''Takes in list of stock prices with daily values in separate lines
            returns list of monthly averages'''
    monthly_vol_x_close = 0
    monthly_volume = 0
    monthly_averages = []

    #before loop, current month is set to first month appearing in file
    current_month = data_list[1][0][0:7]
    
    for line in data_list[1:]:
        if current_month == line[0][:7]:
            #values in each line added to counting variables
            monthly_vol_x_close += float(line[6])*float(line[5])
            monthly_volume += float(line[6])
        else:
            #when new month appears, previous month's values appended to list of averages
            monthly_averages.append((current_month, monthly_vol_x_close/monthly_volume))
            
            #monthly values reset and current month changed
            monthly_vol_x_close = 0
            monthly_volume = 0
            current_month = line[0][:7]
            
            #first values of new month added to counting variables
            monthly_vol_x_close += float(line[6])*float(line[5])
            monthly_volume += float(line[6])
    
    #final month appended to list of averages after exiting loop
    monthly_averages.append((current_month, monthly_vol_x_close/monthly_volume))
    
    return monthly_averages


def print_info(monthly_averages_list):
    '''Takes list of monthly averages and prints values in correct format'''
    print("{:<10s}{:>7s}".format("Month", "Price"))
    for item in monthly_averages_list:
        print("{:<10s}{:>7.2f}".format(item[0], item[1]))


def print_highest(data_list):
    '''Takes in list of stock prices with daily values in separate lines
        prints highest value in specific column after corresponding date'''
    highest = ["",0]
    for line in data_list[1:]:
        if float(line[5]) > highest[1]:
            highest = [line[0], float(line[5])]
    print("Highest price {:.2f} on day {}".format(highest[1], highest[0]))


### MAIN STARTS HERE ###
def main():
    data_list = get_data_list(get_file())
    if data_list:
        monthly_averages_list = get_monthly_averages(data_list)
        print_info(monthly_averages_list)
        print_highest(data_list)
main()