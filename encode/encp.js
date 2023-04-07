/**
 * random value with set
 * @param {*} min min number
 * @param {*} max max number
 * @returns {string} random num
 */
function rand(min, max) {
    return Math.random()*(max-min+1) + min | 0;
}

/**
 * make random salt with set length
 * @param {number} len salt length
 * @returns {string} random salt
 */
function makeSalt(len){
    var str = 'qwertyuiop[]asdfghjkl;zxcvbnm,./';
    var salt = '';
    for(var i=0; i<len; i++){
        salt += str.charAt(rand(0, str.length));
    }
    return salt;
}

/**
 * make salt hash 用密碼加鹽得到雜湊值
 * @param {String} pwd
 * @param {String} salt 
 * @returns hash value
 */
function encodePassword (pwd, salt) {
    return str_md5(pwd + salt);
}

encodePassword("passwd","olsvdwlvi")
'O\x80·ñ\x8Añkâõ<=\x14ÓÄ2ó'