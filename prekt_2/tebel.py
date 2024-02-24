from main import Data_Base
def data():
    buyutrma = f"""
        CREATE TABLE buyurtma(
        buy_id SERIAL PRIMARY KEY,
        nomi VARCHAR(249),
        xarekteri VARCHAR(30),
        yaroqlilik_mudati VARCHAR(40),
        chiqqan_y VARCHAR(30),
        saqlash_mudati VARCHAR(30),
        holati VARCHAR(30)
        );"""
    bolim_ichi = f"""
    CREATE TABLE bolim_ichi(
    bol_id SERIAL PRIMARY KEY,
    nomi VARCHAR(40),
    izox VARCHAR(400),
    mudati VARCHAR(40),
    chiqqan_y VARCHAR(40),
    srogi VARCHAR(40)
    );"""
    bolim = f"""
    CREATE TABLE bolim(
    Bol_id SERIAL PRIMARY KEY,
    kiyim VARCHAR(30),
    poyabzal VARCHAR(30),
    mayshiy_texnika VARCHAR(30),
    elektronika VARCHAR(30),
    bolim_ichi INT REFERENCES bolim_ichi(bol_id)
    );"""
    tolov_j = f"""
    CREATE TABLE tolov_j(
    j_id SERIAL PRIMARY KEY,
    jarayonda VARCHAR(30),
    kutulmoqda VARCHAR(30),
    tolandi VARCHAR(30)
    );"""
    tolov_u = f"""
    CREATE TABLE tolov_u(
    u_id SERIAL PRIMARY KEY,
    payme VARCHAR(30),
    cilik VARCHAR(30),
    tolov_j_id INT REFERENCES tolov_j(j_id)
    );"""
    tolov_t = f"""
    CREATE TABLE tolov_t(
    t_id SERIAL PRIMARY KEY,
    nasiya VARCHAR(30),
    bank VARCHAR(30),
    onlayin VARCHAR(30),
    tolov_u_id INT REFERENCES tolov_u(u_id)
    );"""
    users = f"""
    CREATE TABLE users(
    users_id SERIAL PRIMARY KEY,
    familasi VARCHAR(40),
    T_yili VARCHAR(34),
    pasporst_seria VARCHAR(40),
    viloyat VARCHAR(40),
    tuman VARCHAR(40),
    MFY VARCHAR(40),
    buyurtma_id INT REFERENCES buyurtma(buy_id)
    );"""
    aloqa = f"""
    CREATE TABLE aloqa(
    a_id SERIAL PRIMARY KEY,
    nomer VARCHAR(20),
    manzil VARCHAR(50)
    );"""
    savol_javob = f"""
    CREATE TABLE savol_javob(
    s_id SERIAL PRIMARY KEY,
    royxatdan_otish VARCHAR(500),
    yetkazib_berish VARCHAR(300),
    tolov VARCHAR(89),
    mahsulatlar VARCHAR(300),
    aloqa_id INT REFERENCES aloqa(a_id)
    );"""
    uzum = f"""
    CREATE TABLE uzum(
    id SERIAL PRIMARY KEY,
    usear_id INT REFERENCES users(users_id),
    bolimlar VARCHAR(390),
    bolim_id INT REFERENCES bolim(Bol_id),
    istoriy VARCHAR(40),
    karzinka VARCHAR(290),
    savol_javob_id INT REFERENCES savol_javob(s_id),
    tolov_t_id INT REFERENCES tolov_t(t_id)
    );"""
    tebel = {
        # "buyutrma":buyutrma,
        # "bolim_ichi":bolim_ichi,
        # "bolim":bolim,
        # "tolov_j":tolov_j,
        # "tolov_u": tolov_u,
        # "tolov_t": tolov_t,
        # "users": users,
        # "aloqa":aloqa,
        # "savol_javob":savol_javob,
        "uzum": uzum
    }
    for i in tebel:
        print(f"{i}{Data_Base.DataBase(tebel[i],'insert')}")
if __name__ == "__main__":
    data()