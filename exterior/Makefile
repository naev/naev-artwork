RES := $(if $(HIDPI),800x800,400x400)
PNG_OUTPUTS := $(patsubst %.png,out/%.png,$(wildcard *.png))
JPG_OUTPUTS := $(patsubst %.jpg,out/%.png,$(wildcard *.jpg))
OUTPUTS := $(PNG_OUTPUTS) $(JPG_OUTPUTS)

all: $(OUTPUTS)

out/%.png: %.jpg
	convert -scale $(RES) "$<" "$@"

out/%.png: %.png
	convert -scale $(RES) "$<" "$@"

clean:
	rm -f out/*

.PHONY:
	all clean
