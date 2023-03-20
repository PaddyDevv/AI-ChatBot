

import threading
import requests
import customtkinter

def Send_Message(message):
    cookies = {
        '_ga': 'GA1.1.324017707.1678910368',
        '_ga_B8KFDBZ7TR': 'GS1.1.1678910368.1.0.1678910368.0.0.0',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22186e6db29f6411-09a1775381dc768-7452547c-2073600-186e6db29f7b8b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2ZTZkYjI5ZjY0MTEtMDlhMTc3NTM4MWRjNzY4LTc0NTI1NDdjLTIwNzM2MDAtMTg2ZTZkYjI5ZjdiOGIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22186e6db29f6411-09a1775381dc768-7452547c-2073600-186e6db29f7b8b%22%7D',
    }

    headers = {
        'authority': 'www.aichatting.net',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.1.324017707.1678910368; _ga_B8KFDBZ7TR=GS1.1.1678910368.1.0.1678910368.0.0.0; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22186e6db29f6411-09a1775381dc768-7452547c-2073600-186e6db29f7b8b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2ZTZkYjI5ZjY0MTEtMDlhMTc3NTM4MWRjNzY4LTc0NTI1NDdjLTIwNzM2MDAtMTg2ZTZkYjI5ZjdiOGIifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22186e6db29f6411-09a1775381dc768-7452547c-2073600-186e6db29f7b8b%22%7D',
        'origin': 'https://www.aichatting.net',
        'referer': 'https://www.aichatting.net/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
    }

    json_data = {
        'content': message,
    }

    r = requests.post('https://www.aichatting.net/papi/aigc/chat', cookies=cookies, headers=headers, json=json_data)
    return r.json()['data']['replyContent']

class Gui(customtkinter.CTk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		customtkinter.set_appearance_mode("Dark")
		customtkinter.set_default_color_theme("blue")
        
		self.iconbitmap("Assets/Logo.ico")
		self.title("AI ChatBot")
		self.resizable(0,0)
		self.geometry(f"{250}x{400}")

		# Apikey Label
		self.apikeyLabel = customtkinter.CTkLabel(self, text=" Made By Clumpyㅤㅤㅤㅤㅤㅤㅤ")
		self.apikeyLabel.grid(row=0, column=1, padx=20, pady=20, sticky="ew")





		# Amount Entry Field
		self.ApiKeyEntry = customtkinter.CTkEntry(self, placeholder_text="Hey There!")
		self.ApiKeyEntry.grid(row=1, column=1, columnspan=1, padx=20, pady=20, sticky="ew")


		# Generate Button
		self.generateResultsButton = customtkinter.CTkButton(self, text="Ask AI Question", command=self.MessageSender)
		self.generateResultsButton.grid(row=5, column=1, columnspan=1, padx=20, pady=20, sticky="ew")

		# Result Box
		self.displayBox = customtkinter.CTkTextbox(self, width=220, height=120)
		self.displayBox.grid(row=6, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        

	def MessageSender(self):
		Message = self.ApiKeyEntry.get()
		Resp = Send_Message(Message)
		self.displayBox.insert('0.0', f'You : {Message}\nAI : {Resp}\n')



if __name__ == "__main__":
	app = Gui()
	app.mainloop()
