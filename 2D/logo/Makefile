RES := 256
OUTDIR := ../../out/logo
OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%.webp,$(wildcard *.svg))
OUTPUTS += $(patsubst %.xcf,$(OUTDIR)/%.webp,$(wildcard *.xcf))

SHELL := /usr/bin/bash

all: $(OUTPUTS)
clean:
	rm -f $(OUTPUTS)

test:
	./mkoflag.sh

$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%.webp: $(OUTDIR)/%.png
	cwebp -z 9 "$<" -o "$@"

$(OUTDIR)/%.png: %.svg export.py | $(OUTDIR)
	python export.py "$<" $(RES) "$@" -`./mkoflag.sh`

$(OUTDIR)/%.png: %.xcf logo_xcf2png.sh | $(OUTDIR)
	sh logo_xcf2png.sh "$<" $(RES) "$@"

.PHONY: all clean
