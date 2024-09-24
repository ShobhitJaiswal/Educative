def test(s):
    s = s.split('_')
    a=str(s[0])
    for i in range(1,len(s)):
        a += str(s[i]).capitalize()
    print(a)
    st=""
    for i in a:
        # print(i)
        if i.isupper():
            st+='_'+i.lower()
        else:
            st+=i
    print(st)


test("cagemini_enginnering")
test("capgemini_engineering_pvt_ltd")