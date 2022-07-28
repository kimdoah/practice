try:
    f = open("pension.dat", "rb")
    total = pickle.load(f)
    f.close()
except:
    total = []

for n in range(len(total) + 1, current + 1):
    url = requests.get(
        f"https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%97%B0%EA%B8%88%EB%B3%B5%EA%B6%8C"
    )
    html = BeautifulSoup(url.text)
    numbers = html.find("tr"ㅔ, class_="fst").text.split()[5:]
    numbers[0] = numbers[0].replace("조", "")
    numbers = list(map(int, numbers))
    total.append(numbers)
    print(f"{n}회 로또 python원준에서 바꿈 저장 완료!!! {numbers}")
    time.sleep(1)
    # 피클 저장 사용 => 계속해서 데이터에 저장 - 중단했던 곳 부터 시작
    f = open("pension.dat", "wb")
    pickle.dump(total, f)
