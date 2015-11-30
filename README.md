xiachufang-crawler
================

This is a crawler to get text contents from xiachufang-crawler.  

Using the resources could we do some natural language analysis.

License
------
[The Star And Thank Author License](https://github.com/zTrix/sata-license)

Usage
------
This crawler is based on _scrapy_. 

You can run like this:

```bash
git clone https://github.com/zxteloiv/xiachufang-crawler.git
cd xiachufang-crawler
scrapy crawl recipe
```

Job Control
-----
If you put this scrapy crawler on your VPS, you may use this scripts to start a spider.


```bash
SCRAPY=~/.local/bin/scrapy
JOBDIR=~/job
FILENAME=~/items.json

$SCRAPY crawl recipe -s JOBDIR=$JOBDIR -s PIPELINE_SAVE_FILENAME=$FILENAME
```

If you start like the above, you can press Ctrl-C to stop the spider at any time. The scrapy engine will stop to crawl new pages but still be processing the urls in the queue. When you press the Ctrl-C again it will stop immediately.

You can start the job from where it is stopped last time, use the same command above.

But you can make it run at background using nohup:

```bash
SCRAPY=~/.local/bin/scrapy
JOBDIR=~/job
FILENAME=~/items.json

nohup $SCRAPY crawl recipe -s JOBDIR=$JOBDIR -s PIPELINE_SAVE_FILENAME=$FILENAME &>log &
```

This time, if you want to pause the job, you need to send a Ctrl-C signal to the process.

```bash
ps aux | grep scrapy # find your job pid
kill -SIGINT $PID
```
