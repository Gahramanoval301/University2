zencir_sayi = 7
gunluk_halqa_sayi = 1
otel_gunluk_odeme = 1
def zencir_qirmaq(otel_gunluk_odeme, gunluk_halqa_sayi, zencir_sayi):
    qirmaq_sayi = otel_gunluk_odeme // (gunluk_halqa_sayi * zencir_sayi)
    qalib_otel_gunluk_odeme = otel_gunluk_odeme % (gunluk_halqa_sayi * zencir_sayi)
    return qirmaq_sayi, qalib_otel_gunluk_odeme
qirmaq_sayi, qalib_otel_gunluk_odeme = zencir_qirmaq(otel_gunluk_odeme, gunluk_halqa_sayi, zencir_sayi)
print(f"{zencir_sayi} dənəlik zəncir {qirmaq_sayi} dəfə qırılar və qalıq {qalib_otel_gunluk_odeme} qalır.")