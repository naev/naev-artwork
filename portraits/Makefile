RES := $(if $(HIDPI),400x300,200x150)
OUTPUTS := $(patsubst %.xcf,out/%.png,$(shell find -name '*.xcf'))

all: $(OUTPUTS)

out/%.png: %.xcf
	@mkdir -p "$(dir $@)"
	./xcf2png.sh "$<" "$@" $(RES)

clean:
	rm -rf out/*

.PHONY:
	all clean
