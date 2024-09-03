#include "mock_i2c.h"
#include "am2320.h"
#include <assert.h>

void test_AM2320_Init() {
    I2C_HandleTypeDef hi2c;
    HAL_StatusTypeDef status = AM2320_Init(&hi2c);
    assert(status == HAL_OK);
}

void test_AM2320_ReadTemperature() {
    I2C_HandleTypeDef hi2c;
    float temperature;
    HAL_StatusTypeDef status = AM2320_ReadTemperature(&hi2c, &temperature);
    assert(status == HAL_OK);
    // Additional checks for temperature value can be added
}

int main() {
    test_AM2320_Init();
    test_AM2320_ReadTemperature();
    return 0;
}
