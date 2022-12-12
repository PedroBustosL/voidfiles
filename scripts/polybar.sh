#!/bin/bash

# Terminate all polybar instances

polybar-msg cmd quit


# Launch Bar 1
echo "---" | tee -a /tmp/polybar1.log 
polybar bar1 2>&1 | tee -a /tmp/polybar1.log 

echo "Bar Launched..."
