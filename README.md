# mini-photoshop
Image Processing Project

# swig command
1. python setup_image_processing.py build_ext --inplace  
2. python test.py

# Yang dipanggil sama frontend
Misal nama modulnya image processing, diimportnya as ip
1. Ngelempar array (sekarang defaultnya tipe list / array di python bukan numpy) ke backend
    ip.makeImage(listArrImg, imgType)
    listArrImg -> tipenya list, imgType -> jenis image BINARY, GRAYSCALE, RGB, buat graylevelnya anggep kalo ga 1 bit, 8 bit aja yak, kalo in between ga bisa dibaca sm si PIL nya, gua kebayangnya keluarannya object si image yang dibuat

2. Negative
tinggal panggil self.imageObject.negative() -> modulnya ip.negative()

3. Grayscale
tinggal panggil self.imageObject.grayscale() -> modulnya ip.grayscale()

4. Image Brightener (disatuin yang unbrighten and brighten)
panggil self.imageObject.brightener(int scale) -> scalenya dari -255 sampai 255