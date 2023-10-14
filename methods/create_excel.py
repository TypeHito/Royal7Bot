import xlsxwriter


def row_excel(excel, row, user):
    excel.write(row, 0, str(user[0]))
    excel.write(row, 1, str(user[1]))
    excel.write(row, 2, str(user[2]))
    excel.write(row, 3, str(user[3]))
    excel.write(row, 4, str(user[4]))


def create_excel(user_id, users):
    row = 1
    workbook = xlsxwriter.Workbook(f'files_excel/user_date_{user_id}.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 20)
    worksheet.set_column('H:H', 20)
    worksheet.set_column('J:J', 20)
    worksheet.set_column('I:I', 20)
    worksheet.set_column('K:K', 20)
    worksheet.set_column('L:L', 20)

    worksheet.write(0, 0, "registration_id")
    worksheet.write(0, 1, "telegram_id")
    worksheet.write(0, 2, "phone_number")
    worksheet.write(0, 3, "order_count")
    worksheet.write(0, 4, "gift_type")
    for user in users:
        row_excel(worksheet, row, user)
        row += 1
    workbook.close()
