// 백준 10818
// #include <iostream>

// using namespace std;

// int main() {
//     // N 입력 받기
//     int N;
//     cin >> N;

//     // N의 길이를 갖는 배열 생성
//     int arr[N];

//     // 배열 안에 값 저장
//     for(int i = 0; i < N; i++) {
//         cin >> arr[i];
//     }

//     // Max, Min 값 정의
//     int MX;
//     int MN;

//     // 배열의 0번째 값 Max, Min 설정
//     MX = arr[0];
//     MN = arr[0];

//     // 값 비교하면서 Max, Min 업데이트
//     for(int i = 0; i < N; i++) {
//         if(arr[i] > MX) {
//             MX = arr[i];
//         }
//         if(arr[i] < MN) {
//             MN = arr[i];
//         }
//     }

//     // Min, Max 값 출력
//     cout << MN <<" "<< MX;
// }


#include <iostream>

using namespace std;

int main() {
    // N 입력 받기
    int N;
    cin >> N;

    // Max, Min 값 정의
    int MX;
    int MN;

    // 처음 입력받는 값 MN, MX 설정
    cin >> MX;
    MN = MX;

    int num;

    // 입력받는 값과 MN, MX 비교, 업데이트
    for(int i = 0; i < N-1; i++) {
        cin >> num;
        if (num > MX) {
            MX = num;
        }
        if (num < MN) {
            MN = num;
        }
    }
    cout << MN << " " << MX;
}