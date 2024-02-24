
from Aclass import python, java, c_pilus, c_shar, bepul_kurs, kurslar, royxatdan_otish, tolov_t, tolov_u, oquvchi, oqituvchi, bitirganlar, kirish
def Python():
    son = input(f"""
    1.select
    2.insert
    3.delet
    4.updata
    0.orqaga
    """)
    if son == "1":
        for i in python.select('python'):
            print(i)
            return Python()
    elif son == "2":
        a = input('model_nome: ')
        s = float(input("nech oy bolishi:"))
        d = int(input("necha model:"))
        f = input("narxi: ")
        PYthon = python(a,s,d,f)
        print(PYthon.insert('python'))
        return Python()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "python_id":
            print(python.delete(ustun, qator, "python"))

        else:
            print(python.delete_id(ustun, qator, "python"))
        return Python()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(python.updata(query))
        return Python()
    else:
        return Python()
def Java():
    son = input(f"""
    1.select
    2.insert
    3.delet
    4.updata
    0.orqaga
    """)
    if son == "1":
        for i in java.select('java'):
            print(i)
            return Java()
    elif son == "2":
        a = input('model_nome: ')
        s = float(input("nech oy bolishi:"))
        d = int(input("necha model:"))
        f = input("narxi: ")
        JAva = java(a,s,d,f)
        print(JAva.insert('java'))
        return Java()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "java_id":
            print(java.delete(ustun, qator, "java"))

        else:
            print(java.delete_id(ustun, qator, "java"))
        return Java()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(java.updata(query))
        return Java()
    else:
        return Java()
def C_pilus():
    son = input(f"""
    1.select
    2.insert
    3.delet
    4.updata
    0.orqaga
    """)
    if son == "1":
        for i in c_pilus.select('c_pilus'):
            print(i)
            return C_pilus()
    elif son == "2":
        a = input('model_nome: ')
        s = float(input("nech oy bolishi:"))
        d = int(input("necha model:"))
        f = input("narxi: ")
        C_Pilus = c_pilus(a,s,d,f)
        print(C_Pilus.insert('c_pilus'))
        return C_pilus()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "c_pilus_id":
            print(c_pilus.delete(ustun, qator, "c_pilus"))

        else:
            print(c_pilus.delete_id(ustun, qator, "c_pilus"))
        return C_pilus()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(c_pilus.updata(query))
        return C_pilus()
    else:
        return C_pilus()
def C_shar():
    son = input(f"""
    1.select
    2.insert
    3.delet
    4.updata
    0.orqaga
    """)
    if son == "1":
        for i in c_shar.select('c_shar'):
            print(i)
            return C_shar()
    elif son == "2":
        a = input('model_nome: ')
        s = float(input("nech oy bolishi:"))
        d = int(input("necha model:"))
        f = input("narxi: ")
        C_Shar = c_shar(a,s,d,f)
        print(C_Shar.insert('c_shar'))
        return C_shar()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "c_shar_id":
            print(c_shar.delete(ustun, qator, "c_shar"))

        else:
            print(c_shar.delete_id(ustun, qator, "c_shar"))
        return C_shar()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(c_shar.updata(query))
        return C_shar()
    else:
        return C_shar()
def Bepul_kurs():
    son = input(f"""
      1.select
      2.insert
      3.delet
      4.updata
      0.orqaga
      """)
    if son == "1":
        for i in bepul_kurs.select('bepul_kurs'):
            print(i)
            return Bepul_kurs()
    elif son == "2":
        a = input('model_nome: ')
        s = float(input("nech oy bolishi:"))
        d = int(input("necha model:"))
        f = input("narxi: ")
        Bepul = bepul_kurs(a, s, d, f)
        print(Bepul.insert('bepul_kurs'))
        return Bepul_kurs()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "bepul_kurs_id":
            print(bepul_kurs.delete(ustun, qator, "bepul_kurs"))

        else:
            print(bepul_kurs.delete_id(ustun, qator, "bepul_kurs"))
        return Bepul_kurs()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(bepul_kurs.updata(query))
        return Bepul_kurs()
    else:
        return Bepul_kurs()
def Kurslar():
    son = input(f"""
       1.select
       2.insert
       3.delet
       4.updata
       0.orqaga
       """)
    if son == "1":
        for i in kurslar.select('kurslar'):
            print(i)
            return Kurslar()
    elif son == "2":
        a = int(input('paython: '))
        s = int(input("java:"))
        d = int(input("C_pilus :"))
        f = int(input("c_shar: "))
        g = int(input("bepul_kurslar: "))
        KUrslar = kurslar(a, s, d, f, g)
        print(KUrslar.insert('kurslar'))
        return Kurslar()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "kurs_id":
            print(kurslar.delete(ustun, qator, "kurslar"))

        else:
            print(kurslar.delete_id(ustun, qator, "kurslar"))
        return Kurslar()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(kurslar.updata(query))
        return Kurslar()
    else:
        return Kurslar()
def Royxat():
    son = input(f"""
       1.select
       2.insert
       3.delet
       4.updata
       0.orqaga
       """)
    if son == "1":
        for i in royxatdan_otish.select('royxatdan_otish'):
            print(i)
            return Royxat()
    elif son == "2":
        a = input('ismi: ')
        s = input("familasi:")
        d = input("nomer :")
        f = input("email: ")
        g = input("password: ")
        h = input("adres: ")
        j = int(input("kurs_id: "))
        ROyxat = royxatdan_otish(a, s, d, f, g,h,j)
        print(ROyxat.insert('royxatdan_otish'))
        return Kurslar()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "royxat_id":
            print(royxatdan_otish.delete(ustun, qator, "royxatdan_otish"))

        else:
            print(royxatdan_otish.delete_id(ustun, qator, "royxatdan_otish"))
        return Royxat()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(royxatdan_otish.updata(query))
        return Royxat()
    else:
        return Royxat()
def Tolov_t():
    son = input(f"""
       1.select
       2.insert
       3.delet
       4.updata
       0.orqaga
       """)
    if son == "1":
        for i in tolov_t.select('tolov_t'):
            print(i)
            return Tolov_t()
    elif son == "2":
        a = input('pyme: ')
        s = input("cilik:")
        d = input("paynet :")
        f = input("hisobraqamorqali: ")

        Tolov_T = tolov_t(a, s, d, f)
        print(Tolov_T.insert('tolov_t'))
        return Tolov_t()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "tolov_t_id":
            print(tolov_t.delete(ustun, qator, "tolov_t"))

        else:
            print(tolov_t.delete_id(ustun, qator, "tolov_t"))
        return Tolov_t()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(tolov_t.updata(query))
        return Tolov_t()
    else:
        return Tolov_t()
def Tolov_u():
    son = input(f"""
          1.select
          2.insert
          3.delet
          4.updata
          0.orqaga
          """)
    if son == "1":
        for i in tolov_u.select('tolov_u'):
            print(i)
            return Tolov_u()
    elif son == "2":
        a = input('oyma oy tolash: ')
        s = input("hammasini birdan to'lash:")

        Tolov_U = tolov_t(a, s)
        print(Tolov_U.insert('tolov_u'))
        return Tolov_u()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "tolov_u_id":
            print(tolov_u.delete(ustun, qator, "tolov_u"))

        else:
            print(tolov_u.delete_id(ustun, qator, "tolov_u"))
        return Tolov_u()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(tolov_u.updata(query))
        return Tolov_u()
    else:
        return Tolov_u()
def Oquvchi():
    son = input(f"""
             1.select
             2.insert
             3.delet
             4.updata
             0.orqaga
             """)
    if son == "1":
        for i in oquvchi.select('Oquvchi'):
            print(i)
            return Oquvchi()
    elif son == "2":
        a = input('ismi : ')
        s = input("familasi:")
        d = input("qaysi kursdaligi:")

        OquvchI = oquvchi(a, s,d)
        print(OquvchI.insert('Oquvchi'))
        return Oquvchi()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "oquvchi_id":
            print(oquvchi.delete(ustun, qator, "Oquvchi"))

        else:
            print(oquvchi.delete_id(ustun, qator, "Oquvchi"))
        return Oquvchi()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(oquvchi.updata(query))
        return Oquvchi()
    else:
        return Oquvchi()
def Oqituvchi():
    son = input(f"""
           1.select
           2.insert
           3.delet
           4.updata
           0.orqaga
           """)
    if son == "1":
        for i in oqituvchi.select('oqituvchi'):
            print(i)
            return Oqituvchi()
    elif son == "2":
        a = input('ismi: ')
        s = input("familasi:")
        d = input("mutaxasisligi :")
        f = input("tajribasi: ")
        g = input("staji: ")

        OQituvchi = tolov_t(a, s, d, f, g)
        print(OQituvchi.insert('oqituvchi'))
        return Oqituvchi()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "oqituvchi_id":
            print(oqituvchi.delete(ustun, qator, "oqituvchi"))

        else:
            print(oqituvchi.delete_id(ustun, qator, "oqituvchi"))
        return Oqituvchi()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(oqituvchi.updata(query))
        return Oqituvchi()
    else:
        return Oqituvchi()
def Bitirganlar():
    son = input(f"""
           1.select
           2.insert
           3.delet
           4.updata
           0.orqaga
           """)
    if son == "1":
        for i in bitirganlar.select('bitirganlar'):
            print(i)
            return Oqituvchi()
    elif son == "2":
        a = input('ismi: ')
        s = input("familasi:")
        d = input("qatda ishlashi :")
        f = input("lavozimi: ")
        g = input("maoshi: ")

        BiTirgan = bitirganlar(a, s, d, f, g)
        print(BiTirgan.insert('bitirganlar'))
        return Bitirganlar()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "bitirgan_id":
            print(bitirganlar.delete(ustun, qator, "bitirganlar"))

        else:
            print(bitirganlar.delete_id(ustun, qator, "bitirganlar"))
        return Bitirganlar()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(bitirganlar.updata(query))
        return Bepul_kurs()
    else:
        return Bitirganlar()
def Kkirish():
    son = input(f"""
       1.select
       2.insert
       3.delet
       4.updata
       0.orqaga
       """)
    if son == "1":
        for i in kirish.select('kirish'):
            print(i)
            return Royxat()
    elif son == "2":
        a = input('onlayin kurs: ')
        s = input("talim turi:")
        d = input("oqituvchilar :")
        f = input("natijalar: ")
        g = input("kamment: ")
        h = input("izox: ")
        j = int(input("users_id: "))
        k = int(input("tolov_id: "))
        l = int(input("oqituvchi_id: "))
        z = int(input("oquvchi_id: "))
        x = int(input("bitirgan_id: "))
        Kkkirish = kirish(a, s, d, f, g,h,j,k,l,z,x)
        print(Kkkirish.insert('kirish'))
        return Kkirish()
    elif son == "3":
        ustun = input("column:")
        qator = input("data:")
        if ustun != "ustun_id":
            print(kirish.delete(ustun, qator, "kirish"))

        else:
            print(kirish.delete_id(ustun, qator, "kirish"))
        return Kkirish()

    elif son == "4":
        ustun = input("ustun : ")
        qator = int(input("qator:"))
        query = f""" UPDATE ustun SET name = '{ustun}' WHERE  country_id = {qator};"""
        print(kirish.updata(query))
        return Kkirish()
    else:
        return Kkirish()

def main():
    son = input(f"""
    1.python
    2.java
    3.c_pilus
    4.c_shar
    5.bepul_kurs
    6.kurslar
    7.royxatdan o'tish
    8.tolov_turlari
    9.tolov_usullari
    10.oquvchi
    11.o'qituvchi
    12.bitirganlar
    13.kirish
    0. menyu
    > 
    """)
    if son == '1':
        return Python()
    elif son == '2':
        return Java()
    elif son == '3':
        return C_pilus()
    elif son == '4':
        return C_shar()
    elif son == '5':
         return Bepul_kurs()
    elif son == '6':
        return Kurslar()
    elif son == '7':
        return Royxat()
    elif son == '8':
        return Tolov_t()
    elif son == '9':
        return Tolov_u()
    elif son == '10':
        return Oquvchi()
    elif son == '11':
        return Oqituvchi()
    elif son == '12':
        return Bitirganlar()
    elif son == '13':
        return Kkirish()
    else:
        return  main()
if __name__=="__main__":
    main()