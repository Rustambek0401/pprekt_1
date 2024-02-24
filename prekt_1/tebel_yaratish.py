from PSQL import DataBase
def tebellar():
    python = f"""
        CREATE TABLE python(
            python_id SERIAL PRIMARY KEY,
            model_nomi VARCHAR(30),
            necha_oy_otilishi FLOAT,
            nechta_model SMALLINT,
            narxi VARCHAR(30)
            );
    """
    java = f"""
        CREATE TABLE java(
            java_id SERIAL PRIMARY KEY,
            model_nomi VARCHAR(30),
            necha_oy_otilishi FLOAT,
            nechta_model SMALLINT,
            narxi VARCHAR(30)
            );
    """
    c_pilus = f"""
        CREATE TABLE c_pilus(
            c_pilus_id SERIAL PRIMARY KEY,
            model_nomi VARCHAR(30),
            necha_oy_otilishi FLOAT,
            nechta_model SMALLINT,
            narxi VARCHAR(30)
            );
    """
    c_shar = f"""
        CREATE TABLE c_shar(
            c_shar_id SERIAL PRIMARY KEY,
            model_nomi VARCHAR(30),
            necha_oy_otilishi FLOAT,
            nechta_model SMALLINT,
            narxi VARCHAR(30)
            );
    """
    bepul_kurs = f"""
        CREATE TABLE bepul_kurs (
            bepul_kurs_id SERIAL PRIMARY KEY,
            nomi VARCHAR(30),
            izox VARCHAR(600),
            nechta_dars SMALLINT,
            dars_soni SMALLINT
        );
    """
    kurslar = f"""
        CREATE TABLE kusrlar (
            kusr_id SERIAL PRIMARY KEY,
            python_id INT REFERENCES python(python_id), 
            java_id INT REFERENCES java(java_id), 
            c_pilus_id INT REFERENCES c_pilus(c_pilus_id), 
            c_shar_id INT REFERENCES c_shar(c_shar_id), 
            bepul_kurs INT REFERENCES bepul_kurs(bepul_kurs_id)
            );
        """
    royxatdan_otish = f"""
        CREATE TABLE royxatdan_otish (
            users_id SERIAL PRIMARY KEY,
            ismi VARCHAR(30),
            familasi VARCHAR(40),
            nomeri VARCHAR(10),
            email VARCHAR(30),
            password VARCHAR(10),
            adres VARCHAR(500),
            nima_ishqilishi VARCHAR(200),
            nima_maqsad_uchun_kurs_olopsiz VARCHAR(600),
            kurs_id INT REFERENCES kusrlar(kusr_id));
    """
    tolov_turi = f"""
        CREATE TABLE tolov_turi(
            tolov_turi_id SERIAL PRIMARY KEY,
            pyme VARCHAR(30),
            cilik VARCHAR(30),
            paynet VARCHAR(30),
            bank_orqli VARCHAR(40)
            );"""

    tolov_usuli = f"""
    CREATE TABLE tolov_usuli(
        tolov_u_id SERIAL PRIMARY KEY,
        ismi VARCHAR(20),
        familasi VARCHAR(30),
        qaysi_kursdaligi VARCHAR(50)
         );"""
    bitirganlar = f"""
        CREATE TABLE bitirganlar(
            bitirgan_id SERIAL PRIMARY KEY,
            ismi VARCHAR(29),
            famila VARCHAR(30),
            ishxonasi VARCHAR(30),
            lavozimi VARCHAR(30),
            maoshi VARCHAR(30)); 
            """
    oqituvchi = f"""
        CREATE TABLE oqituvchi(
            oqituvchi SERIAL PRIMARY KEY,
            ismi VARCHAR(29),
            famila VARCHAR(30),
            mutaxasisligi VARCHAR(30),
            tajribasi VARCHAR(30),
            Staji VARCHAR(30)
            );"""
    oquvchi = f"""
        CREATE TABLE oquvchilar(
        oquvchi_id SERIAL PRIMARY KEY,
        ismi VARCHAR(30),
        familasi VARCHAR(30),
        manzili VARCHAR(40),
        email VARCHAR(30)
            );"""
    kirish = f"""
        CREATE TABLE kirish(
            kirish_id SERIAL PRIMARY KEY,
            onlayin_kurslar VARCHAR(50),
            talim_turi VARCHAR(30),
            oqituvchilar SMALLINT,
            oquvchilar_natijasi VARCHAR(200),
            kamment VARCHAR(300),
            izho VARCHAR(1000),
            users_id INT REFERENCES royxatdan_otish(users_id),
            tolov_id INT REFERENCES tolov_usuli(tolov_u_id),
            oquvchi_id INT REFERENCES oquvchilar(oquvchi_id),
            bitirgan_id INT REFERENCES bitirganlar(bitirgan_id),
            oqituvchi_id INT REFERENCES oqituvchi(oqituvchi)
        );"""
    # c = {
#         "python": python,
#         "java": java,
#         "c_pilus": c_pilus,
#         "c_shar": c_shar,
#         "bepul_kurs": bepul_kurs,
#         "kurslar": kurslar,
#         "royxatdan_otish": royxatdan_otish,
#         "tolov_turi": tolov_turi,
#         "tolov_usuli": tolov_usuli,
#         "bitirganlar": bitirganlar,
#         "oqituvchi": oqituvchi,
#         "oquvchi":oquvchi,
#         "kirish": kirish
#     }
#     for i in c:
#         print(f"{i} {DataBase.datbase(c[i],'insert')}")
# if __name__ == "__main__":
#     tebellar()