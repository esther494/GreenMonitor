#include "mock_i2c.h"
#include <stdio.h>

// Mock implementation of HAL_I2C_Master_Transmit
HAL_StatusTypeDef HAL_I2C_Master_Transmit(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout) {
    // Example: Print debug information
    printf("HAL_I2C_Master_Transmit called with Address: %u, Size: %u\n", DevAddress, Size);
    // Return HAL_OK for successful transmission
    return HAL_OK;
}

// Mock implementation of HAL_I2C_Master_Receive
HAL_StatusTypeDef HAL_I2C_Master_Receive(I2C_HandleTypeDef *hi2c, uint16_t DevAddress, uint8_t *pData, uint16_t Size, uint32_t Timeout) {
    // Example: Print debug information
    printf("HAL_I2C_Master_Receive called with Address: %u, Size: %u\n", DevAddress, Size);
    // Simulate received data (e.g., fill with dummy values)
    for (uint16_t i = 0; i < Size; ++i) {
        pData[i] = i; // Example data
    }
    // Return HAL_OK for successful reception
    return HAL_OK;
}

// Mock implementation of HAL_Delay
void HAL_Delay(uint32_t Delay) {
    // Example: Print debug information
    printf("HAL_Delay called with Delay: %lu\n", Delay);
    // Simulate delay (do nothing in mock)
}

