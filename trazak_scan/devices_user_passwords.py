import csv
import database_access_trazak

def process_file_with_users_passwords():
    rownum = 0
    product = ""
    vendor = ""
    device_type = ""
    user_password = ""
    protocol = ""
    with open('/home/MUSA/TRAZAK/ICSecurity/scadapass.csv', 'rb') as csvfile:
        csvReader = csv.reader(csvfile)
        for row in csvReader:
            """lista = list (spamreader)
            print lista [3]
            print lista[4]
            print lista[5]"""
            if rownum > 4:
                colnum = 0
                for col in row:
                    if colnum == 0:
                        vendor = '"' + str(col) + '"'
                    if colnum == 1:
                        product = '"' + str(col) + '"'
                        print "product %s" %product
                    if colnum == 2:
                        user_password = '"' + str(col) + '"'
                    if colnum == 5:
                        device_type = '"' + str(col) + '"'
                    if colnum == 3:
                        protocol = '"' + str(col) + '"'
                    colnum += 1
                # end of if structure
                sentence = "insert into device_password values (%i, %s, %s, %s, %s, %s);" % (rownum, product, vendor, device_type, user_password, protocol)
                print "Sentence %s" % sentence
                database_access_trazak.insert_values(sentence)

            rownum += 1

process_file_with_users_passwords()