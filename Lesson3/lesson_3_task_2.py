from smartphone import Smartphone


cataloge = []

cataloge.append(Smartphone('Apple', 'iPhone X', '+79504422046'))
cataloge.append(Smartphone('Honor', '9 Lite', '+79198765467'))
cataloge.append(Smartphone('Oppo', 'A78', '+79194966907'))
cataloge.append(Smartphone('Samsung', 'Galaxy S24+', '+79223087654'))
cataloge.append(Smartphone('Google', 'Pixel 7a', '+79567654187'))
                
for phone in cataloge:
    print(f"{phone.brand_phone} - {phone.model_phone}, {phone.number}")