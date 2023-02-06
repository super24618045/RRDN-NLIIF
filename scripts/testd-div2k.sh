echo 'div2k-x2' &&
python testwithdata.py --config ./configs/test/test-div2k-2.yaml --model $1 --gpu $2 &&
echo 'div2k-x3' &&
python testwithdata.py --config ./configs/test/test-div2k-3.yaml --model $1 --gpu $2 &&
echo 'div2k-x4' &&
python testwithdata.py --config ./configs/test/test-div2k-4.yaml --model $1 --gpu $2 &&

echo 'div2k-x6*' &&
python testwithdata.py --config ./configs/test/test-div2k-6.yaml --model $1 --gpu $2 &&
echo 'div2k-x12*' &&
python testwithdata.py --config ./configs/test/test-div2k-12.yaml --model $1 --gpu $2 &&
echo 'div2k-x18*' &&
python testwithdata.py --config ./configs/test/test-div2k-18.yaml --model $1 --gpu $2 &&
echo 'div2k-x24*' &&
python testwithdata.py --config ./configs/test/test-div2k-24.yaml --model $1 --gpu $2 &&
echo 'div2k-x30*' &&
python testwithdata.py --config ./configs/test/test-div2k-30.yaml --model $1 --gpu $2 &&

true
