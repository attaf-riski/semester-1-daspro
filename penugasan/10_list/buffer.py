#[1,2,3,4,5]
        #konso(5,inverse([1,2,3,4]))
        #konso(5,konso(4,inverse([1,2,3])))
        #konso(5,konso(4,konso(3,inverse([1,2]))))
        #konso(5,konso(4,konso(3,konso(2,inverse([1])))))
        #konso(5,konso(4,konso(3,konso(2,konso(1,inverse([]))))))
        #konso(5,konso(4,konso(3,konso(2,konso(1,[])))))
        #konso(5,konso(4,konso(3,konso(2,[1]))))
        #konso(5,konso(4,konso(3,[2,1])))
        #konso(5,konso(4,[3,2,1]))
        #konso(5,[4,3,2,1])
        #[5,4,3,2,1]