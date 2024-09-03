# 0 "src/am2320.c"
# 0 "<built-in>"
# 0 "<command-line>"
# 1 "src/am2320.c"
# 1 "include/mock_i2c.h" 1



# 1 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stdint.h" 1 3 4
# 9 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stdint.h" 3 4
# 1 "C:/msys64/ucrt64/include/stdint.h" 1 3 4
# 28 "C:/msys64/ucrt64/include/stdint.h" 3 4
# 1 "C:/msys64/ucrt64/include/crtdefs.h" 1 3 4
# 10 "C:/msys64/ucrt64/include/crtdefs.h" 3 4
# 1 "C:/msys64/ucrt64/include/corecrt.h" 1 3 4
# 10 "C:/msys64/ucrt64/include/corecrt.h" 3 4
# 1 "C:/msys64/ucrt64/include/_mingw.h" 1 3 4
# 10 "C:/msys64/ucrt64/include/_mingw.h" 3 4
# 1 "C:/msys64/ucrt64/include/_mingw_mac.h" 1 3 4
# 98 "C:/msys64/ucrt64/include/_mingw_mac.h" 3 4
             
# 107 "C:/msys64/ucrt64/include/_mingw_mac.h" 3 4
             
# 302 "C:/msys64/ucrt64/include/_mingw_mac.h" 3 4
       
# 381 "C:/msys64/ucrt64/include/_mingw_mac.h" 3 4
       
# 11 "C:/msys64/ucrt64/include/_mingw.h" 2 3 4
# 1 "C:/msys64/ucrt64/include/_mingw_secapi.h" 1 3 4
# 12 "C:/msys64/ucrt64/include/_mingw.h" 2 3 4
# 282 "C:/msys64/ucrt64/include/_mingw.h" 3 4
# 1 "C:/msys64/ucrt64/include/vadefs.h" 1 3 4
# 9 "C:/msys64/ucrt64/include/vadefs.h" 3 4
# 1 "C:/msys64/ucrt64/include/_mingw.h" 1 3 4
# 661 "C:/msys64/ucrt64/include/_mingw.h" 3 4
# 1 "C:/msys64/ucrt64/include/sdks/_mingw_ddk.h" 1 3 4
# 662 "C:/msys64/ucrt64/include/_mingw.h" 2 3 4
# 10 "C:/msys64/ucrt64/include/vadefs.h" 2 3 4




#pragma pack(push,_CRT_PACKING)
# 24 "C:/msys64/ucrt64/include/vadefs.h" 3 4
  
# 24 "C:/msys64/ucrt64/include/vadefs.h" 3 4
 typedef __builtin_va_list __gnuc_va_list;






  typedef __gnuc_va_list va_list;
# 103 "C:/msys64/ucrt64/include/vadefs.h" 3 4
#pragma pack(pop)
# 283 "C:/msys64/ucrt64/include/_mingw.h" 2 3 4
# 580 "C:/msys64/ucrt64/include/_mingw.h" 3 4
void __attribute__((__cdecl__)) __debugbreak(void);
extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) void __attribute__((__cdecl__)) __debugbreak(void)
{

  __asm__ __volatile__("int {$}3":);







}
# 601 "C:/msys64/ucrt64/include/_mingw.h" 3 4
void __attribute__((__cdecl__)) __attribute__ ((__noreturn__)) __fastfail(unsigned int code);
extern __inline__ __attribute__((__always_inline__,__gnu_inline__)) void __attribute__((__cdecl__)) __attribute__ ((__noreturn__)) __fastfail(unsigned int code)
{

  __asm__ __volatile__("int {$}0x29"::"c"(code));
# 615 "C:/msys64/ucrt64/include/_mingw.h" 3 4
  __builtin_unreachable();
}
# 641 "C:/msys64/ucrt64/include/_mingw.h" 3 4
const char *__mingw_get_crt_info (void);
# 11 "C:/msys64/ucrt64/include/corecrt.h" 2 3 4




#pragma pack(push,_CRT_PACKING)
# 35 "C:/msys64/ucrt64/include/corecrt.h" 3 4
__extension__ typedef unsigned long long size_t;
# 45 "C:/msys64/ucrt64/include/corecrt.h" 3 4
__extension__ typedef long long ssize_t;






typedef size_t rsize_t;
# 62 "C:/msys64/ucrt64/include/corecrt.h" 3 4
__extension__ typedef long long intptr_t;
# 75 "C:/msys64/ucrt64/include/corecrt.h" 3 4
__extension__ typedef unsigned long long uintptr_t;
# 88 "C:/msys64/ucrt64/include/corecrt.h" 3 4
__extension__ typedef long long ptrdiff_t;
# 98 "C:/msys64/ucrt64/include/corecrt.h" 3 4
typedef unsigned short wchar_t;







typedef unsigned short wint_t;
typedef unsigned short wctype_t;





typedef int errno_t;




typedef long __time32_t;




__extension__ typedef long long __time64_t;
# 138 "C:/msys64/ucrt64/include/corecrt.h" 3 4
typedef __time64_t time_t;
# 430 "C:/msys64/ucrt64/include/corecrt.h" 3 4
struct threadlocaleinfostruct;
struct threadmbcinfostruct;
typedef struct threadlocaleinfostruct *pthreadlocinfo;
typedef struct threadmbcinfostruct *pthreadmbcinfo;
struct __lc_time_data;

typedef struct localeinfo_struct {
  pthreadlocinfo locinfo;
  pthreadmbcinfo mbcinfo;
} _locale_tstruct,*_locale_t;



typedef struct tagLC_ID {
  unsigned short wLanguage;
  unsigned short wCountry;
  unsigned short wCodePage;
} LC_ID,*LPLC_ID;




typedef struct threadlocaleinfostruct {

  const unsigned short *_locale_pctype;
  int _locale_mb_cur_max;
  unsigned int _locale_lc_codepage;
# 482 "C:/msys64/ucrt64/include/corecrt.h" 3 4
} threadlocinfo;
# 501 "C:/msys64/ucrt64/include/corecrt.h" 3 4
#pragma pack(pop)
# 11 "C:/msys64/ucrt64/include/crtdefs.h" 2 3 4
# 29 "C:/msys64/ucrt64/include/stdint.h" 2 3 4



# 1 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stddef.h" 1 3 4
# 1 "C:/msys64/ucrt64/include/stddef.h" 1 3 4
# 18 "C:/msys64/ucrt64/include/stddef.h" 3 4
  __attribute__ ((__dllimport__)) extern int *__attribute__((__cdecl__)) _errno(void);

  errno_t __attribute__((__cdecl__)) _set_errno(int _Value);
  errno_t __attribute__((__cdecl__)) _get_errno(int *_Value);


  __attribute__ ((__dllimport__)) extern unsigned long __attribute__((__cdecl__)) __threadid(void);

  __attribute__ ((__dllimport__)) extern uintptr_t __attribute__((__cdecl__)) __threadhandle(void);
# 2 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stddef.h" 2 3 4
# 426 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stddef.h" 3 4
typedef struct {
  long long __max_align_ll __attribute__((__aligned__(__alignof__(long long))));
  long double __max_align_ld __attribute__((__aligned__(__alignof__(long double))));
# 437 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stddef.h" 3 4
} max_align_t;
# 33 "C:/msys64/ucrt64/include/stdint.h" 2 3 4


typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef short int16_t;
typedef unsigned short uint16_t;
typedef int int32_t;
typedef unsigned uint32_t;
__extension__ typedef long long int64_t;
__extension__ typedef unsigned long long uint64_t;


typedef signed char int_least8_t;
typedef unsigned char uint_least8_t;
typedef short int_least16_t;
typedef unsigned short uint_least16_t;
typedef int int_least32_t;
typedef unsigned uint_least32_t;
__extension__ typedef long long int_least64_t;
__extension__ typedef unsigned long long uint_least64_t;





typedef signed char int_fast8_t;
typedef unsigned char uint_fast8_t;
typedef short int_fast16_t;
typedef unsigned short uint_fast16_t;
typedef int int_fast32_t;
typedef unsigned int uint_fast32_t;
__extension__ typedef long long int_fast64_t;
__extension__ typedef unsigned long long uint_fast64_t;


__extension__ typedef long long intmax_t;
__extension__ typedef unsigned long long uintmax_t;
# 10 "C:/msys64/ucrt64/lib/gcc/x86_64-w64-mingw32/13.2.0/include/stdint.h" 2 3 4
# 5 "include/mock_i2c.h" 2


# 6 "include/mock_i2c.h"
typedef enum {
    HAL_OK = 0x00U,
    HAL_ERROR = 0x01U,
    HAL_BUSY = 0x02U,
    HAL_TIMEOUT = 0x03U
} HAL_StatusTypeDef;

typedef struct {

    uint8_t Dummy;
} I2C_HandleTypeDef;


HAL_StatusTypeDef HAL_I2C_Master_Transmit(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout);
HAL_StatusTypeDef HAL_I2C_Master_Receive(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout);
void HAL_Delay(uint32_t Delay);
# 2 "src/am2320.c" 2
# 1 "include/am2320.h" 1






# 1 "include/mock_i2c.h" 1
# 8 "include/am2320.h" 2

HAL_StatusTypeDef AM2320_Init(I2C_HandleTypeDef *hi2c);
HAL_StatusTypeDef AM2320_ReadTemperature(I2C_HandleTypeDef *hi2c, float *temperature);
HAL_StatusTypeDef AM2320_ReadHumidity(I2C_HandleTypeDef *hi2c, float *humidity);
HAL_StatusTypeDef AM2320_ReadTemperatureAndHumidity(I2C_HandleTypeDef *hi2c, float *temperature, float *humidity);
# 3 "src/am2320.c" 2

extern I2C_HandleTypeDef hi2c1;

uint8_t txBuffer[1] = {0x02};

HAL_StatusTypeDef AM2320_Init(I2C_HandleTypeDef *hi2c) {
 return HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, 0x00, 0, HAL_MAX_DELAY);
}

HAL_StatusTypeDef AM2320_ReadTemperature(I2C_HandleTypeDef *hi2c, float *temperature) {

 uint8_t msg[3] = {0x03, 0x02, 0x02};
 uint8_t temp_data[8];

 HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, txBuffer, 0, HAL_MAX_DELAY);
 HAL_Delay(1);


    if (HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, msg, 3, HAL_MAX_DELAY) != HAL_OK) {
        return HAL_ERROR;
    }
    HAL_Delay(2);


    if (HAL_I2C_Master_Receive(hi2c, 0x5C << 1, temp_data, 8, HAL_MAX_DELAY) != HAL_OK) {
        return HAL_ERROR;
    }
    HAL_Delay(2);


    uint16_t raw_temp = (temp_data[2] << 8) | temp_data[3];
    *temperature = (float) raw_temp / 10;

    return HAL_OK;
}

HAL_StatusTypeDef AM2320_ReadHumidity(I2C_HandleTypeDef *hi2c, float *humidity) {

 uint8_t msg[3] = {0x03, 0x00, 0x02};
 uint8_t humidity_data[8];

 HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, 0x00, 0, HAL_MAX_DELAY);
 HAL_Delay(1);


    if (HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, msg, 3, HAL_MAX_DELAY) != HAL_OK) {
        return HAL_ERROR;
    }
    HAL_Delay(2);


    if (HAL_I2C_Master_Receive(hi2c, 0x5C << 1, humidity_data, 8, HAL_MAX_DELAY) != HAL_OK) {
        return HAL_ERROR;
    }
    HAL_Delay(2);


    uint16_t raw_humidity = (humidity_data[2] << 8) | humidity_data[3];
    *humidity = (float) raw_humidity / 10;

    return HAL_OK;
}

HAL_StatusTypeDef AM2320_ReadTemperatureAndHumidity(I2C_HandleTypeDef *hi2c, float *temperature, float *humidity) {
    uint8_t txBuffer[3] = {0x03, 0x00, 0x04};
    uint8_t dataBuffer[8];

 HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, 0x00, 0, HAL_MAX_DELAY);
 HAL_Delay(1);


    if (HAL_I2C_Master_Transmit(hi2c, 0x5C << 1, txBuffer, sizeof(txBuffer), HAL_MAX_DELAY) != HAL_OK) {
        return HAL_ERROR;
    }


    HAL_Delay(2000);


    if (HAL_I2C_Master_Receive(hi2c, 0x5C << 1, dataBuffer, sizeof(dataBuffer), HAL_MAX_DELAY) != HAL_OK) {
        return HAL_ERROR;
    }




    uint16_t raw_humidity = (dataBuffer[2] << 8) | dataBuffer[3];
    uint16_t raw_temperature = (dataBuffer[4] << 8) | dataBuffer[5];

    *humidity = (float) raw_humidity / 10.0;
    *temperature = (float) raw_temperature / 10.0;

    return HAL_OK;
}
