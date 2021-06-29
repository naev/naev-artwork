RES_TINY := $(if $(HIDPI),48,24)
RES_SMALL := $(if $(HIDPI),128,64)
OUTDIR := ../../out/logo
TINY_OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%_tiny.png,$(wildcard *.svg))
TINY_OUTPUTS += $(patsubst %.xcf,$(OUTDIR)/%_tiny.png,$(wildcard *.xcf))
SMALL_OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%_small.png,$(wildcard *.svg))
SMALL_OUTPUTS += $(patsubst %.xcf,$(OUTDIR)/%_small.png,$(wildcard *.xcf))
OUTPUTS := $(TINY_OUTPUTS) $(SMALL_OUTPUTS)

all: $(OUTPUTS)
clean:
	rm -f $(OUTPUTS)

$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%_tiny.png: %.svg export.py | $(OUTDIR)
	python export.py "$<" $(RES_TINY) "$@"

$(OUTDIR)/%_small.png: %.svg export.py | $(OUTDIR)
	python export.py "$<" $(RES_SMALL) "$@"

$(OUTDIR)/%_tiny.png: %.xcf logo_xcf2png.sh | $(OUTDIR)
	sh logo_xcf2png.sh "$<" $(RES_TINY) "$@"

$(OUTDIR)/%_small.png: %.xcf logo_xcf2png.sh | $(OUTDIR)
	sh logo_xcf2png.sh "$<" $(RES_SMALL) "$@"

.PHONY: all clean
