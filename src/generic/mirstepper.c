#include "stm32f4xx_hal.h" // Include the appropriate header for your STM32 MCU
#include <stdint.h>

class StepperMotor {
private:
    TIM_HandleTypeDef htim; // Timer handle
    GPIO_TypeDef *port;     // GPIO port for step pin
    uint16_t stepPin;       // GPIO pin for step pin
    uint32_t currentPos;    // Current position of the motor
    uint32_t targetPos;     // Target position of the motor
    uint32_t speed;         // Speed of the motor (steps per second)
    uint32_t acceleration;  // Acceleration of the motor (steps per second squared)
    uint32_t stepInterval;  // Time interval between steps (in microseconds)
    uint32_t lastStepTime;  // Timestamp of the last step

public:
    // Constructor to initialize the stepper motor object
    StepperMotor(TIM_HandleTypeDef htim_, GPIO_TypeDef *port_, uint16_t stepPin_)
        : htim(htim_), port(port_), stepPin(stepPin_) {
        // Initialize motor parameters
        currentPos = 0;
        targetPos = 0;
        speed = 0;
        acceleration = 0;
        stepInterval = 0;
        lastStepTime = 0;

        // Configure GPIO pin as output
        GPIO_InitTypeDef GPIO_InitStruct;
        GPIO_InitStruct.Pin = stepPin;
        GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
        GPIO_InitStruct.Pull = GPIO_NOPULL;
        GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
        HAL_GPIO_Init(port, &GPIO_InitStruct);
    }

    // Set the target position for the motor
    void moveToPos(uint32_t pos) {
        targetPos = pos;
        // Calculate new speed and step interval
        calculateSpeed();
    }

    // Set the current position of the motor
    void setPos(uint32_t pos) {
        currentPos = pos;
    }

    // Set the speed of the motor (steps per second)
    void setSpeed(uint32_t speed_) {
        speed = speed_;
        // Recalculate step interval
        calculateStepInterval();
    }

    // Set the acceleration of the motor (steps per second squared)
    void setAcceleration(uint32_t acceleration_) {
        acceleration = acceleration_;
        // Recalculate step interval
        calculateStepInterval();
    }

    // Move the motor according to the speed and acceleration
    void move() {
        uint32_t currentTime = HAL_GetTick();
        uint32_t elapsedTime = currentTime - lastStepTime;

        // Check if it's time to take the next step
        if (elapsedTime >= stepInterval) {
            HAL_GPIO_WritePin(port, stepPin, GPIO_PIN_SET); // Step high
            HAL_Delay(1); // Adjust this delay as needed for motor stability
            HAL_GPIO_WritePin(port, stepPin, GPIO_PIN_RESET); // Step low

            // Update current position
            if (currentPos < targetPos)
                currentPos++;
            else if (currentPos > targetPos)
                currentPos--;

            // Calculate new speed and step interval
            calculateSpeed();

            // Update last step time
            lastStepTime = currentTime;
        }
    }

private:
    // Calculate the speed and step interval based on current position and target position
    void calculateSpeed() {
        // Calculate distance to target position
        int32_t distance = targetPos - currentPos;

        // Determine direction of movement
        int8_t direction = (distance > 0) ? 1 : (distance < 0) ? -1 : 0;

        // Calculate new speed
        if (acceleration != 0) {
            speed = (speed < abs(acceleration) * abs(distance)) ? speed + acceleration : speed;
        }

        // Calculate new step interval
        if (speed != 0) {
            stepInterval = 1000000 / speed; // Convert speed to microseconds
        }
    }
};

int main() {
    // Initialize HAL
    HAL_Init();

    // Initialize timer for precise timing
    TIM_HandleTypeDef htim;
    // Initialize GPIO pins
    GPIO_TypeDef *stepPort = GPIOA; // Example: using GPIOA
    uint16_t stepPin = GPIO_PIN_0; // Example: using pin 0

    // Create a StepperMotor object for your stepper motor
    StepperMotor motor(htim, stepPort, stepPin);

    // Example usage: move to position 1000 with speed 500 steps per second and acceleration 100 steps per second squared
    motor.moveToPos(1000);
    motor.setSpeed(500);
    motor.setAcceleration(100);

    while (1) {
        motor.move();
    }

    return 0;
}
