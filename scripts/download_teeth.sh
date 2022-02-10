mkdir temp
git clone https://github.com/M2-IGAI2022/teeth-database.git temp
unzip temp/img_align_teeth.zip -d ./data/databases/teeth
rm -r temp -f