import asyncio
import base64
import json
import logging
import os

import requests
from requests_toolbelt import MultipartEncoder

from wwai_sdk import utils
from wwai_sdk.cache import WwaiSdkCache
from wwai_sdk.decrypt_util import decrypt_rsa, decrypt_aes

logger = logging.getLogger(__name__)

class WwaiClient:
    def __init__(self,
                 grant_type,
                 server="http://ai.api.wwai.wwxckj.com",
                 authorization=None,
                 username=None,
                 password=None,
                 tenant_code=None,
                 client_id=None,
                 client_secret=None,
                 cache_type="local",
                 redis_host=None,
                 redis_port=6379,
                 redis_password=None,
                 redis_db=0,
                 rsa_private_key=None):
        self.cache = WwaiSdkCache(cache_type, redis_host, redis_port, redis_password, redis_db)
        self.server = server
        self.grant_type = grant_type
        self.authorization = authorization
        self.username = username
        self.password = password
        self.tenant_code = tenant_code
        self.client_id = client_id
        self.client_secret = client_secret
        self.rsa_private_key = rsa_private_key
        self.get_token()

    def get_token(self):
        """
        获取Token
        :return:
        """
        access_token = self.cache.get(f"{self.tenant_code}-access_token")
        if access_token:
            return access_token, self.cache.get(f"{self.tenant_code}-tenant_id")
        headers = {
            "Authorization": self.authorization,
            "Content-Type": 'application/x-www-form-urlencoded'
        }
        if self.grant_type == 'password':
            payload = {
                "grant_type": "password",
                "username": self.username,
                "password": self.password,
                "tenant_code": self.tenant_code
            }
        else:
            payload = {
                "grant_type": "client_credentials"
            }
        response = requests.post(
            f"{self.server}/auth/oauth2/token",
            headers=headers,
            data=payload,
            verify=False
        )
        if response.ok:
            response_data = response.json()
            if "access_token" in response_data:
                access_token = f"Bearer {response_data.get('access_token', '')}"
                tenant_id = response_data.get("tenant_id", None)
                access_token_expire = int(response_data.get("expires_in", "0"))
                access_token_expire = access_token_expire - 60
                self.cache.set(f"{self.tenant_code}-access_token", access_token, access_token_expire)
                if tenant_id:
                    self.cache.set(f"{self.tenant_code}-tenant_id", tenant_id)
                return access_token, tenant_id
            else:
                raise ValueError(f"WWAI云平台参数错误：{response.status_code} {response.text}")
        else:
            raise ValueError(f"WWAI云平台登陆异常：{response.status_code} {response.text}")



    def _request(self, url: str, params=None, json=None, data=None, files=None, headers=None, method="GET", all_result=False):
        """
        发送请求
        :return:
        """
        base_url = self.server
        if base_url.endswith("/"):
            base_url = base_url[:-1]
        if url.startswith("/"):
            url = url[1:]
        api_url = f"{base_url}/{url}"

        if headers is None:
            headers = {}
        access_token, tenant_id = self.get_token()
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'
        headers['Authorization'] = f"{access_token}"
        if tenant_id is not None:
            headers['Tenant-ID'] = tenant_id

        resp = requests.request(method, api_url, params=params, json=json, data=data, files=files, headers=headers, verify=False)
        if resp.ok:
            resp = resp.json()
            code = int(resp.get("code", "500"))
            if code != 0 and code != 200:
                if resp["msg"] == "用户凭证已过期":
                    self.cache.delete(f"{self.tenant_code}-access_token")
                    self.cache.delete(f"{self.tenant_code}-tenant_id")
                raise Exception(resp["msg"])
            else:
                return resp if all_result else resp['data']
        else:
            raise Exception(resp.text)

    async def ocr_idcard(self, image_url, side=None):
        """
        身份证识别
        :param image_url:
        :param side:
        :return:
        """
        req = {
            "image": image_url,
            "side": side
        }
        return await asyncio.to_thread(self._request, "/open/ocr/idcard", json=req, method="POST")

    async def ocr_vehicle(self, image_url: str):
        """
        行驶证识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/vehicle", json=req, method="POST")

    async def ocr_driving_license(self, image_url: str, side: str = "front"):
        """
        驾驶证识别
        :param image_url:
        :param side:
        :return:
        """
        req = {
            "image": image_url,
            "side": side
        }
        return await asyncio.to_thread(self._request, "/open/ocr/driving_license", json=req, method="POST")

    async def ocr_vehicle_certificate(self, image_url: str):
        """
        机动车登记证书识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/vehicle_certificate", json=req, method="POST")

    async def ocr_invoice(self, image_url: str):
        """
        发票识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/invoice", json=req, method="POST")

    async def ocr_bank_card(self, image_url: str):
        """
        银行卡识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/bank", json=req, method="POST")

    async def other_classify(self, image_url):
        """
        通用图片分类
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/image_classify", json=req, method="POST")

    async def ocr_img_quality(self, image_url: str, image_type: str):
        """
        图片质量检测
        :param image_url:
        :param image_type:
        :return:
        """
        req = {
            "image": image_url,
            "image_type": image_type
        }
        return await asyncio.to_thread(self._request, "/open/ocr/img_quality", json=req, method="POST")

    async def ocr_cards_correction(self, image_url: str):
        """
        卡证矫正
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/cards_correction", json=req, method="POST")

    async def ocr_cards_angle(self, image_url: str):
        """
        证件倾斜角度检测
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/cards_angle", json=req, method="POST")

    async def ocr_car_plate_detection(self, image_url: str):
        """
        车牌检测
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/car_plate_detection", json=req, method="POST")

    async def ocr_common(self, image_url: str):
        """
        通用文字识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/common", json=req, method="POST")

    async def ocr_chat_ocr(self, image_url: str):
        """
        关键信息识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/chat_ocr", json=req, method="POST")

    async def ocr_handwriting(self, image_url):
        """
        手写文字识别
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/handwriting", json=req, method="POST")

    async def ocr_entity_mosaic(self, image_url: str):
        """
        图像实体信息打码
        :param image_url:
        :return:
        """
        req = {
            "image": image_url
        }
        return await asyncio.to_thread(self._request, "/open/ocr/entity_mosaic", json=req, method="POST")


    async def speech_asr_iat(self, audio: str):
        """
        语音识别
        :return:
        """
        try:
            import wave
        except ImportError:
            raise ImportError("Please install wave with `pip install wave`")

        if not audio:
            return
        if utils.is_url(audio):
            audio = utils.down_bytes(audio)
            audio = base64.b64encode(audio).decode()
        if not isinstance(audio, str):
            raise ValueError("audio must be base64 or url")

        try:
            res = await asyncio.to_thread(self._request, "/open/speech/asr_iat", data={"audio": audio}, method="POST",
                                headers={"Content-Type": "application/x-www-form-urlencoded"})
            logger.info(f"=======>wwai asr res: {res}")
            return res
        except Exception as e:
            logger.error(f"wwai asr error: {e}")
            raise e

    async def face_compare_face_image(self, image1:str, image2:str, image_type="url", tolerance=0.6):
        """
        人脸图片比对
        :param image1:
        :param image2:
        :param image_type:
        :param tolerance:
        :return:
        """
        req = {
            "image1": image1,
            "image2": image2,
            "image_type": image_type,
            "tolerance": tolerance
        }
        return await asyncio.to_thread(self._request, "/open/face/compare_face_image", json=req, method="POST")

    async def tts_offline(self, text, spk_id=174, am="fastspeech2_mix", voc="hifigan_csmsc", lang="mix", speed=1):
        """
        离线语音合成
        :param text:
        :param spk_id:
        :param am:
        :param voc:
        :param lang:
        :param speed:
        :return:
        """
        req = {
            "text": text,
            "spk_id": spk_id,
            "am": am,
            "voc": voc,
            "lang": lang,
            "speed": speed
        }
        return await asyncio.to_thread(self._request, "/open/tts/offline", json=req, method="POST")

    async def aigc_models(self, model_type=None):
        """
        获取可用的模型列表
        :param model_type:
        :return:
        """
        req = {}
        if model_type:
            if model_type not in ["text", "vl", "embedding"]:
                raise ValueError("model_type must be text or vl or embedding")
            req["modelType"] = model_type
        return await asyncio.to_thread(self._request, "/open/aigc/models", params=req)

    async def llm_generate(self, prompt: str):
        """
        大模型文本生成
        :param prompt:
        :return:
        """
        req = {
            "prompt": prompt
        }
        return await asyncio.to_thread(self._request, "/open/llm/generate", json=req, method="POST")

    async def llm_car_info_identify(self, car_detail: str):
        """
        基于大模型判断文本中的信息是否与车有关
        :param car_detail:
        :return:
        """
        req = {
            "car_detail": car_detail
        }
        return await asyncio.to_thread(self._request, "/open/llm/car_info_identify", json=req, method="POST")

    async def llm_text_extract_json(self, text: str, fields: str | list):
        """
        基于大模型提取文本中的关键信息
        :param text:
        :param fields:
        :return:
        """
        if isinstance(fields, list):
            fields = ",".join(fields)
        req = {
            "text": text,
            "fields": fields
        }
        return await asyncio.to_thread(self._request, "/open/llm/text_extract_json", json=req, method="POST")

    async def llm_sensitive_word_detection(self, words_content: str):
        """
        基于大模型检测文本中是否包含敏感词
        :param words_content:
        :return:
        """
        req = {
            "words_content": words_content
        }
        return await asyncio.to_thread(self._request, "/open/llm/sensitive_word_detection", json=req, method="POST")

    async def huaweicloud_obs_get_ak_sk(self, bucket_name, endpoint=None):
        """
        获取临时OBS的 AK/SK
        :param bucket_name:
        :param endpoint:
        :return:
        """
        req = {
            "bucketName": bucket_name
        }
        if endpoint:
            req["endpoint"] = endpoint
        else:
            req["endpoint"] = "obs.cn-north-4.myhuaweicloud.com"

        res = await asyncio.to_thread(self._request, "/open/huaweicloud/getObsTempAkSk", json=req, method="POST", all_result=True)
        aes_key_encrypt_data = res.get("aesKey", "")
        encrypt_data = res.get("data", "")

        aes_key = decrypt_rsa(aes_key_encrypt_data, self.rsa_private_key)
        data = decrypt_aes(encrypt_data, aes_key)

        return json.loads(data)

    async def data_center_dealer_address(self, dealer: str, managerName: str):
        """
        获取车商地址
        :param dealer:
        :param managerName:
        :return:
        """
        req = {
            "dealer": dealer,
            "managerName": managerName
        }
        return await asyncio.to_thread(self._request, "/open/data/center/dealer_address", json=req, method="POST")

    async def common_word2html(self, word_path):
        """
        word转html
        :param word_path:
        :return:
        """
        if not os.path.exists(word_path):
            raise FileNotFoundError(f"文件{word_path}不存在")
        filename = os.path.basename(word_path)
        data = MultipartEncoder(
            fields={
                "file": (filename, open(word_path, "rb"))
            }
        )
        access_token, tenant_id = self.get_token()
        headers = {
            "Content-Type": data.content_type,
            "Authorization": f"Bearer {access_token}"
        }
        if tenant_id:
            headers["Tenant-Id"] = tenant_id
        resp = await asyncio.to_thread(requests.post, f"{self.server}/open/common/word2html", data=data, headers=headers, verify=False)
        if resp.ok:
            b = resp.content
            html = b.decode("utf-8")
            return html
        else:
            logger.error(f"word转html失败: {resp.text}")
            raise Exception(resp.text)

    async def common_word2docx(self, word_path):
        """
        word转docx
        :param word_path:
        :return:
        """
        if not os.path.exists(word_path):
            raise FileNotFoundError(f"文件{word_path}不存在")
        filename = os.path.basename(word_path)
        data = MultipartEncoder(
            fields={
                "file": (filename, open(word_path, "rb"))
            }
        )
        access_token, tenant_id = self.get_token()
        headers = {
            "Content-Type": data.content_type,
            "Authorization": f"Bearer {access_token}"
        }
        if tenant_id:
            headers["Tenant-Id"] = tenant_id
        resp = await asyncio.to_thread(requests.post, f"{self.server}/open/common/word2docx", data=data, headers=headers, verify=False)
        if resp.ok:
            docx_path = f"{word_path}.docx"
            with open(docx_path, "wb") as f:
                f.write(resp.content)
            return docx_path
        else:
            logger.error(f"word转docx失败: {resp.text}")
            raise Exception(resp.text)

    async def common_word2pdf(self, word_path: str, pdf_path: None):
        """
        word转pdf
        :param word_path:
        :return:
        """
        if not os.path.exists(word_path):
            raise FileNotFoundError(f"文件{word_path}不存在")
        filename = os.path.basename(word_path)
        data = MultipartEncoder(
            fields={
                "file": (filename, open(word_path, "rb"))
            }
        )
        access_token, tenant_id = self.get_token()
        headers = {
            "Content-Type": data.content_type,
            "Authorization": f"Bearer {access_token}"
        }
        if tenant_id:
            headers["Tenant-Id"] = tenant_id
        resp = await asyncio.to_thread(requests.post, f"{self.server}/open/common/doc2pdf", data=data, headers=headers, verify=False)
        if resp.ok:
            if not pdf_path:
                pdf_path = f"{word_path}.pdf"
            with open(pdf_path, "wb") as f:
                f.write(resp.content)
            return pdf_path
        else:
            logger.error(f"word转pdf失败: {resp.text}")
            raise Exception(resp.text)

    async def common_cp_user(self, agentid, code, state=None):
        """
        获取企业用户信息
        :param agentid:
        :param code:
        :return:
        """
        data = {
            "agentid": agentid,
            "code": code,
            "state": state
        }
        resp = await asyncio.to_thread(self._request, "/open/oauth2/cp/verifyCode", params=data, method='GET')
        if resp.get("uuid", ""):
            return resp
        raise Exception("获取企业用户信息失败")
