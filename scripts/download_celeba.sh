mkdir temp
git clone https://github.com/M2-IGAI2022/celeba-database.git temp
unzip temp/img_align_celeba.zip -d ./data/databases/celeba
rm -r temp -f