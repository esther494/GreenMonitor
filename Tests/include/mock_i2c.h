#ifndef MOCK_HAL_H
#define MOCK_HAL_H

#include <stdint.h>
#define HAL_MAX_DELAY 0xFFFFFFFFU
typedef enum {
    HAL_OK       = 0x00U,
    HAL_ERROR    = 0x01U,
    HAL_BUSY     = 0x02U,
    HAL_TIMEOUT  = 0x03U
} HAL_StatusTypeDef;

typedef struct {
    // Define the structure as needed, or leave it empty if it's not used
    uint8_t Dummy;
} I2C_HandleTypeDef;

// Mock function prototypes
HAL_StatusTypeDef HAL_I2C_Master_Transmit(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout);
HAL_StatusTypeDef HAL_I2C_Master_Receive(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout);
void HAL_Delay(uint32_t Delay);

#endif // MOCK_HAL_H
