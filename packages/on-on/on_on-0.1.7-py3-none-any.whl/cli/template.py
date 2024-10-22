from cli.maker import make
from datetime import date

# Yeni oluşturulacak olan depoların referans alacağı fonksiyondur.
def template(project_name: str = "."):    
    # README.md
    make.file(make.absjoiner([project_name, "README.md"]), f"# {project_name}")
    today = date.today()

    # tarihlere göre listele
    tarihlere_gore_listele = make.absjoiner([project_name, "tarihlere-gore-listele"])
    tarih_listelemenin_gun_elemani = make.absjoiner([tarihlere_gore_listele, str(today)])
    make.dir(tarihlere_gore_listele) 
    make.dir(tarih_listelemenin_gun_elemani)
    make.file(make.absjoiner([tarih_listelemenin_gun_elemani, "not1.md"]), f"# {project_name}\n\n> [!NOTE {today} / 00:00-00:01 tarihli ders notları]")
    
    # konulara göre listele
    konulara_gore_listele = make.absjoiner([project_name, "konulara-gore-listele"])
    ders_konusu = make.absjoiner([konulara_gore_listele, "giris"])
    make.dir(konulara_gore_listele) 
    make.dir(ders_konusu)
    make.file(make.absjoiner([ders_konusu, "not1.md"]), f"# {project_name}\n\n> [!NOTE {today} / 00:00-00:01 tarihli ders notları]")
