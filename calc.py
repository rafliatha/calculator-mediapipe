import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inisialisasi OpenCV untuk menggambar di layar
mp_drawing = mp.solutions.drawing_utils

# Fungsi untuk mendeteksi angka berdasarkan posisi jari
def detect_number(landmarks):
    finger_tips = [4, 8, 12, 16, 20]  # Indeks jari telunjuk, jari tengah, dll
    finger_states = []

    for tip in finger_tips:
        finger_pos = landmarks[tip]
        # Tentukan logika untuk mendeteksi apakah jari terangkat atau tidak
        if finger_pos.y < landmarks[tip-2].y:
            finger_states.append(1)  # Jari terangkat
        else:
            finger_states.append(0)  # Jari turun

    # Mengonversi posisi jari yang terdeteksi menjadi angka
    number = sum(finger_states)  # Sederhana, jumlahkan jari yang terangkat
    return number

# Fungsi untuk menangani operasi matematika
def perform_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Div by Zero'
    else:
        return 'Invalid Operator'

# Buka kamera dan deteksi tangan
cap = cv2.VideoCapture(0)

# Variabel untuk menyimpan input
current_number = 0
previous_number = None
operator = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Konversi ke RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Deteksi tangan
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Deteksi angka berdasarkan posisi jari
            number = detect_number(landmarks.landmark)
            
            # Menampilkan angka yang terdeteksi
            cv2.putText(frame, f'Angka: {number}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            # Gambar landmark tangan
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Menyimpan angka untuk operasi kalkulator
            if operator is None:
                current_number = number  # Angka pertama
            else:
                previous_number = current_number
                current_number = number
            
            # Menentukan operator berdasarkan gesture tangan (misalnya gesture jari terbuka sepenuhnya)
            if number == 5:  # Asumsi: angka 5 = operator tambah "+"
                operator = "+"
                cv2.putText(frame, f'Operator: {operator}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            elif number == 10:  # Asumsi: angka 10 = operator kurang "-"
                operator = "-"
                cv2.putText(frame, f'Operator: {operator}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            elif number == 15:  # Asumsi: angka 15 = operator kali "*"
                operator = "*"
                cv2.putText(frame, f'Operator: {operator}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            elif number == 20:  # Asumsi: angka 20 = operator bagi "/"
                operator = "/"
                cv2.putText(frame, f'Operator: {operator}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Jika operator dan angka sudah lengkap, lakukan operasi
            if previous_number is not None and operator is not None:
                result = perform_operation(previous_number, current_number, operator)
                cv2.putText(frame, f'Hasil: {result}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                previous_number = None
                operator = None
    
    # Tampilkan frame
    cv2.imshow("Hand Tracking Calculator", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
