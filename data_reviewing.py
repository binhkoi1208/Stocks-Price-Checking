import yfinance as yf
import matplotlib.pyplot as plt

available_data = ["HIGH", "LOW", "OPEN", "CLOSE", "VOLUME"]
colors = ['red', 'blue', 'green', 'cyan', 'black']
mean = {
    "High": "giá cổ phiếu cao nhất trong từng ngày",
    "Low": "giá cổ phiếu thấp nhất trong từng ngày",
    "Open": "giá cổ phiếu khi mở đầu phiên của từng ngày",
    "Close": "giá cổ phiếu khi kết thúc phiên của từng ngày",
    "Volume": "lượng giao dịch trong từng ngày"
}

company_number = int(input("Nhập số lượng công ty bạn muốn đối chiếu (Nhỏ hơn 5): "))

def get_data(name, data_want_to_see):
    ticker = yf.Ticker(name)
    data = ticker.history(period = "3mo", interval = "1d")

    if data.empty:
        return None
    else:
        data_ret = []
        for date, view in data[data_want_to_see.capitalize()].items():
            data_ret.append(view)

        return data_ret
       
def get_date():
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period = "3mo", interval = "1d")

    date_ret = []
    for date, view in data["Volume"].items():
        date_ret.append(date)

    return date_ret

def get_info(name):
    ticker = yf.Ticker(name)
    
    ret_inf = ticker.info.get("longName")

    return ret_inf

if company_number > 5:
    company_number = int(input("Số lượng quá 5, vui lòng nhập lại: "))
else:
    try:
        data_requested = input("Nhập loại số liệu bạn muốn xem: ")

        if data_requested.upper() not in available_data:
            print("Loại số liệu không tồn tại!")
        else:
            company = []
            for i in range(company_number):
                company.append(input(f"Nhập tên công ty thứ {i + 1}: ").upper())

            date = get_date()

            plt.figure(figsize=(12, 8))
            hdln = ""
            sdln = ""
            for i in range(company_number):
                if get_data(company[i], data_requested) == None:
                    print(f"Công ty {company[i]} không tồn tại")
                    continue
                else:
                    plt.plot(date, get_data(company[i], data_requested), linewidth = 2.0, color = colors[i], label = company[i])

                    hdln += get_info(company[i])
                    hdln += "; "

                    sdln += company[i]
                    sdln += ", "

            hdln = hdln[:-2]
            sdln = sdln[:-2]

            if company_number == 1:
                company_number = ""
            else:
                company_number = " " + str(company_number)

            plt.grid(True)
            plt.title(f"Số liệu về {mean[data_requested.capitalize()]} của{company_number} công ty {hdln} trong 3 tháng gần đây")
            plt.xlabel("Ngày - Tháng - Năm")
            plt.ylabel(f"{mean[data_requested.capitalize()].capitalize()} của{company_number} mã cổ phiếu {sdln}")       
            plt.legend() 

            save_qes = input("Bạn có muốn lưu biểu đồ không (Yes / No)? ")
            if save_qes.upper() == "YES":
                plt.savefig("gia tri co phieu.png")
                plt.show()
            else:
                plt.show()

    except:
        print("Nhập quá số lượng công ty!")

