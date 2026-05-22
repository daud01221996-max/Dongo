import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def print_log(text):
    print(text, flush=True)
    sys.stdout.flush()

def run_bot():
    # Daftar 119 link video manual kamu
    video_links = [
        "https://www.febspot.com/video/3218504", "https://www.febspot.com/video/3218505",
        "https://www.febspot.com/video/3218527", "https://www.febspot.com/video/3218528",
        "https://www.febspot.com/video/3216677", "https://www.febspot.com/video/3217419",
        "https://www.febspot.com/video/3217420", "https://www.febspot.com/video/3217423",
        "https://www.febspot.com/video/3217424", "https://www.febspot.com/video/3189338", 
        "https://www.febspot.com/video/3189741", "https://www.febspot.com/video/3189743",
        "https://www.febspot.com/video/3189744", "https://www.febspot.com/video/3189747", 
        "https://www.febspot.com/video/3189748", "https://www.febspot.com/video/3189750", 
        "https://www.febspot.com/video/3189751", "https://www.febspot.com/video/3189753",
        "https://www.febspot.com/video/3189754", "https://www.febspot.com/video/3189846", 
        "https://www.febspot.com/video/3189848", "https://www.febspot.com/video/3189849", 
        "https://www.febspot.com/video/3189851", "https://www.febspot.com/video/3189857",
        "https://www.febspot.com/video/3189858", "https://www.febspot.com/video/3189860", 
        "https://www.febspot.com/video/3189861", "https://www.febspot.com/video/3189863", 
        "https://www.febspot.com/video/3189864", "https://www.febspot.com/video/3183766",
        "https://www.febspot.com/video/3185499", "https://www.febspot.com/video/3185507", 
        "https://www.febspot.com/video/3185508", "https://www.febspot.com/video/3185510", 
        "https://www.febspot.com/video/3185511", "https://www.febspot.com/video/3185512",
        "https://www.febspot.com/video/3189317", "https://www.febspot.com/video/3189318", 
        "https://www.febspot.com/video/3189319", "https://www.febspot.com/video/3189320", 
        "https://www.febspot.com/video/3189321", "https://www.febspot.com/video/3189328",
        "https://www.febspot.com/video/3189329", "https://www.febspot.com/video/3189330", 
        "https://www.febspot.com/video/3189331", "https://www.febspot.com/video/3189333", 
        "https://www.febspot.com/video/3189334", "https://www.febspot.com/video/3189335",
        "https://www.febspot.com/video/3189336", "https://www.febspot.com/video/3181867", 
        "https://www.febspot.com/video/3181868", "https://www.febspot.com/video/3182071", 
        "https://www.febspot.com/video/3182072", "https://www.febspot.com/video/3182073",
        "https://www.febspot.com/video/3182075", "https://www.febspot.com/video/3182076", 
        "https://www.febspot.com/video/3182077", "https://www.febspot.com/video/3182079", 
        "https://www.febspot.com/video/3182080", "https://www.febspot.com/video/3182081",
        "https://www.febspot.com/video/3182082", "https://www.febspot.com/video/3182083", 
        "https://www.febspot.com/video/3182086", "https://www.febspot.com/video/3182087", 
        "https://www.febspot.com/video/3182089", "https://www.febspot.com/video/3182091",
        "https://www.febspot.com/video/3182092", "https://www.febspot.com/video/3182093", 
        "https://www.febspot.com/video/3183764", "https://www.febspot.com/video/3171758", 
        "https://www.febspot.com/video/3171759", "https://www.febspot.com/video/3171760",
        "https://www.febspot.com/video/3171761", "https://www.febspot.com/video/3171762", 
        "https://www.febspot.com/video/3181098", "https://www.febspot.com/video/3181099", 
        "https://www.febspot.com/video/3181100", "https://www.febspot.com/video/3181101",
        "https://www.febspot.com/video/3181102", "https://www.febspot.com/video/3181103", 
        "https://www.febspot.com/video/3181104", "https://www.febspot.com/video/3181106", 
        "https://www.febspot.com/video/3181108", "https://www.febspot.com/video/3181109",
        "https://www.febspot.com/video/3181860", "https://www.febspot.com/video/3181861", 
        "https://www.febspot.com/video/3181863", "https://www.febspot.com/video/3181865", 
        "https://www.febspot.com/video/3181866", "https://www.febspot.com/video/3141597",
        "https://www.febspot.com/video/3141598", "https://www.febspot.com/video/3141600", 
        "https://www.febspot.com/video/3141605", "https://www.febspot.com/video/3141763", 
        "https://www.febspot.com/video/3141777", "https://www.febspot.com/video/3141780",
        "https://www.febspot.com/video/3144339", "https://www.febspot.com/video/3144340", 
        "https://www.febspot.com/video/3144342", "https://www.febspot.com/video/3144343", 
        "https://www.febspot.com/video/3144347", "https://www.febspot.com/video/3144349",
        "https://www.febspot.com/video/3171613", "https://www.febspot.com/video/3171614", 
        "https://www.febspot.com/video/3171617", "https://www.febspot.com/video/3171618", 
        "https://www.febspot.com/video/3171620", "https://www.febspot.com/video/3171623",
        "https://www.febspot.com/video/3171624", "https://www.febspot.com/video/3137143", 
        "https://www.febspot.com/video/3137150", "https://www.febspot.com/video/3137152", 
        "https://www.febspot.com/video/3137158", "https://www.febspot.com/video/3137159",
        "https://www.febspot.com/video/3137164", "https://www.febspot.com/video/3141573", 
        "https://www.febspot.com/video/3141576", "https://www.febspot.com/video/3141587", 
        "https://www.febspot.com/video/3141592"
    ]

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    print_log(">>> Menyiapkan Browser...")
    driver = webdriver.Chrome(options=chrome_options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    try:
        # 1. AMBIL TAMBAHAN LINK DARI HALAMAN PROFIL
        profile_url = "https://www.febspot.com/heru01221996"
        print_log(f">>> Mengecek profil untuk link tambahan: {profile_url}")
        driver.get(profile_url)
        time.sleep(7)

        last_count = 0
        same_count_retry = 0
        for i in range(15):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            
            elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/video/')]")
            current_count = len(set([el.get_attribute("href") for el in elements if el.get_attribute("href")]))
            
            if current_count == last_count:
                same_count_retry += 1
                if same_count_retry >= 3: break
            else:
                same_count_retry = 0
            last_count = current_count

            try:
                load_more_btn = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Load more')]")))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", load_more_btn)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", load_more_btn)
                time.sleep(5)
            except:
                break

        scraped_links = [el.get_attribute("href") for el in driver.find_elements(By.XPATH, "//a[contains(@href, '/video/')]") if el.get_attribute("href")]
        video_links = list(set(video_links + scraped_links))
        
        print_log(f">>> TOTAL AKHIR: {len(video_links)} video siap diputar.")
        print_log("-" * 40)

        # 2. PROSES LOOPING PEMUTARAN
        random.shuffle(video_links)
        main_window = driver.current_window_handle

        for index, link in enumerate(video_links):
            print_log(f"\n[{index+1}/{len(video_links)}] Membuka: {link}")
            driver.get(link)
            time.sleep(5) 
            
            try:
                wait = WebDriverWait(driver, 15)
                
                # 🔘 PROSES KLIK TOMBOL GERBANG IKLAN
                accept_btn = driver.find_elements(By.XPATH, "//button[contains(text(), 'Accept & Watch Video')]")
                if not accept_btn:
                    accept_btn = driver.find_elements(By.XPATH, "//div[contains(@class, 'watched')]//button")
                
                if accept_btn and accept_btn[0].is_displayed():
                    print_log("🔘 Menemukan tombol iklan. Mengklik 'Accept & Watch Video'...")
                    driver.execute_script("arguments[0].click();", accept_btn[0])
                    
                    # 🔥 PERUBAHAN 1: SENGGJA TUNGGU DI TAB IKLAN DULU (8 DETIK) SEBELUM DITUTUP
                    print_log("⏳ Menahan tab iklan terbuka selama 8 detik agar valid...")
                    time.sleep(8) 
                    
                    if len(driver.window_handles) > 1:
                        print_log("🗂️ Menutup tab iklan baru dan kembali fokus...")
                        all_handles = driver.window_handles
                        for handle in all_handles:
                            if handle != main_window:
                                driver.switch_to.window(handle)
                                driver.close() 
                        
                        driver.switch_to.window(main_window)
                        time.sleep(2)

                # 📺 MONITORING ELEMEN VIDEO UTAMA
                video_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
                
                # 🔥 PERUBAHAN 2: DETEKSI DETIK BERJALAN UNTUK MEMASTIKAN VIDEO TIDAK MACET
                print_log("🔍 Memeriksa status putaran video...")
                time.sleep(3) # Jeda sebentar untuk melihat pergerakan detik awal
                
                check_time_1 = driver.execute_script("return arguments[0].currentTime;", video_element)
                time.sleep(3)
                check_time_2 = driver.execute_script("return arguments[0].currentTime;", video_element)
                
                # Jika detik waktu tidak bertambah atau video dalam posisi pause, paksa klik play manual
                is_paused = driver.execute_script("return arguments[0].paused;", video_element)
                if check_time_1 == check_time_2 or is_paused:
                    print_log("⚠️ Video terdeteksi diam/macet. Memicu klik play manual...")
                    actions = ActionChains(driver)
                    actions.move_to_element(video_element).click().perform()
                    time.sleep(2)
                else:
                    print_log("▶️ Konfirmasi: Video berjalan otomatis dengan baik.")

                duration = driver.execute_script("return arguments[0].duration;", video_element)
                if duration and duration > 0:
                    print_log(f"⏳ Durasi Video: {int(duration)} detik.")
                    start_watch = time.time()
                    
                    while True:
                        current = driver.execute_script("return arguments[0].currentTime;", video_element)
                        ended = driver.execute_script("return arguments[0].ended;", video_element)
                        
                        if ended or current >= (duration - 1):
                            print_log("✅ Selesai Menonton.")
                            break
                        
                        if (time.time() - start_watch) > (duration + 20):
                            print_log("⏱️ Batas waktu tayang maksimal tercapai.")
                            break
                        time.sleep(4)
                else:
                    time.sleep(25)
                    print_log("✅ Selesai Menonton (Waktu Cadangan).")
                    
            except Exception as e:
                print_log("❌ Terjadi kendala saat memproses elemen video.")
            
            time.sleep(random.randint(4, 7))

    except Exception as e:
        print_log(f"💥 GLOBAL ERROR: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    run_bot()
