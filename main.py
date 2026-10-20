"""
Studi Kasus Materi 1: Make Sense of Data with Analysis and AI
Topik: Analisis Data Penjualan untuk Mendukung Pengambilan Keputusan

Program ini mendemonstrasikan:
- Data preparation: memeriksa nilai kosong, duplikat, dan nilai tidak valid
- Descriptive analytics: menghitung omzet, produk terlaris, dan tren bulanan
- Insight dan rekomendasi sederhana berdasarkan hasil analisis
"""

import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data_penjualan.csv"


def load_data(path):
    """Membaca data transaksi dari file CSV."""
    df = pd.read_csv(path)
    print("=== PEMERIKSAAN DATA AWAL ===")
    print(f"Jumlah baris awal: {len(df)}")
    print(f"Nilai kosong per kolom:\n{df.isna().sum()}")
    print(f"Jumlah baris duplikat: {df.duplicated().sum()}")
    return df


def prepare_data(df):
    """Membersihkan data agar layak dianalisis."""
    cleaned = df.copy()

    # Hapus baris duplikat
    cleaned = cleaned.drop_duplicates()

    # Ubah kolom tanggal menjadi format tanggal
    cleaned["tanggal"] = pd.to_datetime(cleaned["tanggal"], errors="coerce")

    # Ubah kolom numerik; data yang tidak dapat dikonversi menjadi nilai kosong
    cleaned["jumlah"] = pd.to_numeric(cleaned["jumlah"], errors="coerce")
    cleaned["harga_satuan"] = pd.to_numeric(cleaned["harga_satuan"], errors="coerce")

    # Buang baris yang memiliki kolom penting kosong/tidak valid
    cleaned = cleaned.dropna(
        subset=["tanggal", "produk", "jumlah", "harga_satuan"]
    )
    cleaned = cleaned[
        (cleaned["produk"].astype(str).str.strip() != "")
        & (cleaned["jumlah"] > 0)
        & (cleaned["harga_satuan"] >= 0)
    ]

    cleaned["produk"] = cleaned["produk"].astype(str).str.strip()
    cleaned["omzet"] = cleaned["jumlah"] * cleaned["harga_satuan"]

    print("\n=== HASIL DATA PREPARATION ===")
    print(f"Jumlah baris setelah dibersihkan: {len(cleaned)}")
    print(f"Baris yang tidak digunakan: {len(df) - len(cleaned)}")
    return cleaned


def analyze_data(df):
    """Melakukan analisis deskriptif terhadap data penjualan."""
    total_omzet = df["omzet"].sum()
    total_transaksi = len(df)
    total_unit = df["jumlah"].sum()

    sales_by_product = (
        df.groupby("produk", as_index=False)
        .agg(total_unit=("jumlah", "sum"), total_omzet=("omzet", "sum"))
        .sort_values("total_omzet", ascending=False)
    )

    df["bulan"] = df["tanggal"].dt.to_period("M").astype(str)
    monthly_sales = (
        df.groupby("bulan", as_index=False)["omzet"]
        .sum()
        .sort_values("bulan")
    )

    print("\n=== HASIL ANALISIS DESKRIPTIF ===")
    print(f"Total omzet: Rp{total_omzet:,.0f}")
    print(f"Jumlah baris transaksi: {total_transaksi}")
    print(f"Total unit terjual: {total_unit:g}")

    print("\nPenjualan berdasarkan produk:")
    print(sales_by_product.to_string(index=False))

    print("\nOmzet berdasarkan bulan:")
    print(monthly_sales.to_string(index=False))

    return sales_by_product, monthly_sales, total_omzet


def make_recommendation(sales_by_product, monthly_sales):
    """Menyusun rekomendasi sederhana berdasarkan hasil analisis."""
    print("\n=== INSIGHT DAN REKOMENDASI ===")

    if not sales_by_product.empty:
        top_product = sales_by_product.iloc[0]
        print(
            f"- Produk dengan omzet tertinggi adalah {top_product['produk']} "
            f"dengan omzet Rp{top_product['total_omzet']:,.0f}."
        )
        print(
            "- Toko dapat mempertimbangkan menjaga ketersediaan produk tersebut "
            "dan memeriksa apakah permintaannya konsisten."
        )

    if len(monthly_sales) >= 2:
        first = monthly_sales.iloc[0]
        last = monthly_sales.iloc[-1]
        if last["omzet"] > first["omzet"]:
            trend = "meningkat"
        elif last["omzet"] < first["omzet"]:
            trend = "menurun"
        else:
            trend = "relatif tetap"
        print(
            f"- Omzet bulan terakhir pada data {trend} dibandingkan bulan pertama. "
            "Periksa faktor promosi, stok, dan jumlah transaksi sebelum mengambil keputusan."
        )

    print(
        "- Rekomendasi ini merupakan indikasi awal dari data, bukan bukti sebab-akibat. "
        "Keputusan akhir tetap memerlukan pemeriksaan konteks bisnis oleh manusia."
    )


def main():
    raw_data = load_data(DATA_FILE)
    clean_data = prepare_data(raw_data)
    if clean_data.empty:
        print("Tidak ada data valid untuk dianalisis. Periksa file CSV.")
        return

    product_summary, monthly_summary, total_omzet = analyze_data(clean_data)
    make_recommendation(product_summary, monthly_summary)

    # Simpan hasil agar dapat diperiksa kembali
    output_dir = Path(__file__).parent / "hasil"
    output_dir.mkdir(exist_ok=True)
    clean_data.to_csv(output_dir / "data_penjualan_bersih.csv", index=False)
    product_summary.to_csv(output_dir / "ringkasan_per_produk.csv", index=False)
    monthly_summary.to_csv(output_dir / "ringkasan_per_bulan.csv", index=False)
    print(f"\nFile hasil analisis tersimpan di: {output_dir}")


if __name__ == "__main__":
    main()
