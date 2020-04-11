RES := $(if $(HIDPI),400x300,200x150)
OUTDIR := ../../out/portraits
SOURCES := $(shell find -name '*.xcf')
OUTPUTS := $(patsubst %.xcf,$(OUTDIR)/%.png,$(SOURCES))

all: $(OUTPUTS)

$(OUTDIR)/%.png: %.xcf background.png xcf2png.sh
	@mkdir -p "$(dir $@)"
	./xcf2png.sh "$<" "$@" $(RES)

.PHONY: all
