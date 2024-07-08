# python300_11~50
# python300_11~20_변수
# python300_21~50_문자열

# 11
삼성전자 = 50000
print(삼성전자*10)

# 12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.70

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13
s = 'hello'
t = 'python'

print(s+'!', t)

# 15
a = 128
print(type(a))
a = "132"
print(type(a))

# 16
num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))

# 17
num = 100
num_str = str(num)
print(num_str, type(num_str))

# 18
str01 = "15.79"
str01_flo = float(str01)
print(str01_flo, type(str01_flo))

# 19 
year = '2020'
year_int = int(year)
print(year_int-3, year_int-2, year_int-1)

# 20
price = 48584
pay = 36
sum_price = price*pay
print(sum_price)

# 21 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])

# 22 문자열 슬라이싱
license_plate = "24가 2210"
print(license_plate[-4:])

# 23 문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[::2])   # 시작인덱스:끝인덱스:오프셋 지정
print(string[::3])   # 홀 짝
print(string[1::2])   # 짝짝짝

# 24 문자열 슬라이싱
string = "PYTHON"
print(string[::-1])

# 25 문자열 치환
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 26 문자열 다루기
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)

# 27 문자열 다루기
url = "http://sharebook.kr"
print(url[-2:])   # 방법1 : 슬라이싱

url_split = url.split('.')  # 방법2: split으로 분리
print(url_split[-1])

# 28 문자열은 immutable
lang = 'python'
lang[0] = 'P'   # 문자열은 할당 메서드를 지원하지 않음. 따라서 수정할 수 없다. 
print(lang)

# 29 replace 메서드
string = 'abcdfe2a354a32a'
string2 = string.replace("a", "A")
print(string2)

# 30 replace 메서드
string = 'abcd'
string.replace('b', '8')   # 문자열은 변경할 수 없는 자료형이므로! 원본은 그대로 둔채로 변경된 새로운 문자열을 리턴해줌.
print(string)     # abcd가 그대로 출력된다. 

# 31 문자열 합치기 - 결과 예상해보기
a = "3"
b = "4"
print(a + b)

# 32 문자열 곱하기 - 결과 예상해보기
print("Hi" * 3)

# 33 문자열 곱하기 - 화면에 '-' 80개 출력
print("-" * 80)

# 34 문자열 더하기, 곱하기 
t1 = 'python'
t2 = 'java'
print((t1, t2) * 4)
t3 = t1 + ' ' + t2
print(t3 * 4)

# 35 문자열 출력 - % formatting
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 36 문자열 출력 - format() 메서드
user1 = "이름: {} 나이: {}".format(name1, age1)
print(user1)

print("이름: {} 나이: {}".format(name2, age2))

# 37 문자열 출력 - f-string
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38 컴마 제거하기
상장주식수 = "5,969,782,550"
no_comma = 상장주식수.replace(",", "")
int_no_comma = int(no_comma)
print(int_no_comma, type(int_no_comma))

# 39 문자열 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40 strip 메서드 - strip() 메서드를 사용하면 좌우 공백 제거 가능. 원본 문자열은 그대로 유지되고, 공백 제거된 새로운 문자열이 반환됨.
data = "   삼성전자    "
print(data.strip())

# 41 upper 메서드
ticker = "btc_krw"
print(ticker.upper())

# 42 lower 메서드
ticker = "BTC_KRW"
print(ticker.lower())

# 43 capitalize 메서드
str_cap = 'hello'
str_cap2 = str_cap[0].upper() + str_cap[1:]
print(str_cap2)

a = 'hello'
a = a.capitalize()
print(a)

# 44 endswith 메서드
file_name = "보고서.xlsx"
file_name.endswith("xlsx")

# 45 endswith 메서드
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))

# 46 startswith 메서드
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")

# 47 split 메서드
a = "hello world"
a.split()

# 48 split 메서드
ticker = "btc_krw"
ticker.split("_")

# 49 split 메서드
date = "2020-05-01"
date.split("-")

# 50 rstrip 메서드
data = "039490     "
data.rstrip()