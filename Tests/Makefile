CC = gcc
CFLAGS = -Iinclude -Iunity -Wall -Wextra -std=c99
LDFLAGS =

SOURCES = src/mock_i2c.c tests/test_am2320.c tests/test_main.c src/am2320.c
OBJECTS = $(SOURCES:.c=.o)
TARGET = test_executable

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(TARGET) $(OBJECTS)
