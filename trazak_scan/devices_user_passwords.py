import csv

def process_file_with_users_passwords():
    sentence = "insert into device (" \
               "module_oem_id,module_serial,module_name," \
               "module_type,plant_id,copyright,ip, scanning_port)values (&module_oem_id&,&module_serial&,&module_name&," \
               "&module_type&,&plant_id&,&copyright&,&ip&,&scanning_port&);"
    with open('/home/MUSA/TRAZAK/ICSecurity/scadapass.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)

process_file_with_users_passwords()