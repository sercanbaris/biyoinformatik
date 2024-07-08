#!/bin/bash

# Çıktı dosyasının adını belirle
output_file="dosya_boyutlari.csv"

# CSV başlığını oluştur
echo "Dosya Adı,Boyut (MB)" > "$output_file"

# Klasördeki her dosya için döngü
for file in *; do
    # Dosya ise (dizin değilse) işlem yap
    if [ -f "$file" ]; then
        # Dosya boyutunu MB cinsinden hesapla (1 ondalık basamakla)
        size=$(du -m "$file" | cut -f1)
        size_mb=$(echo "scale=1; $size / 1" | bc)
        
        # Dosya adı ve boyutunu CSV'ye ekle
        echo "\"$file\",$size_mb" >> "$output_file"
    fi
done

echo "İşlem tamamlandı. Sonuçlar $output_file dosyasına kaydedildi."
