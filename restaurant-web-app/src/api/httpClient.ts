/* eslint-disable @typescript-eslint/no-explicit-any */
import { toast } from 'sonner';

const BASE_API_URL = 'http://127.0.0.1:5000';

export type RequestResponse = { success: boolean; data?: any; error?: any };

interface HeaderType {
  Authorization?: string;
  'Content-Type'?: string;
  responseType?: 'json' | 'blob';
}

export interface IHTTPClient {
  get: (
    url: string,
    query?: string,
    options?: HeaderType
  ) => Promise<RequestResponse>;
  post: <T>(
    url: string,
    body: T,
    options?: HeaderType
  ) => Promise<RequestResponse>;
  put: <T>(
    url: string,
    body: T,
    options?: HeaderType
  ) => Promise<RequestResponse>;
  patch: <T>(
    url: string,
    body: T,
    options?: HeaderType
  ) => Promise<RequestResponse>;
  delete: (url: string, options?: HeaderType) => Promise<RequestResponse>;
}

class HTTPClient implements IHTTPClient {
  base_url;
  onError;

  constructor(onError?: (res: RequestResponse) => void) {
    this.onError = onError;

    if (!BASE_API_URL) {
      throw new Error('Base url is not provided');
    }
    this.base_url = BASE_API_URL;
  }

  async request(
    method: string,
    url: string,
    body?: any,
    xheaders?: HeaderType & { responseType?: 'json' | 'blob' }
  ): Promise<RequestResponse> {
    try {
      let isFormData = false;

      if (body instanceof FormData) {
        isFormData = true;
      }

      const requestOptions: RequestInit = {
        method,
        headers: {
          ...(!isFormData ? { 'Content-Type': 'application/json' } : {}),
          ...xheaders,
          'Cache-Control': 'no-cache',
          Pragma: 'no-cache',
        },
        cache: 'no-store',
        body: body ? (!isFormData ? JSON.stringify(body) : body) : undefined,
      };

      const response = await fetch(`${this.base_url}/${url}`, requestOptions);
	  console.log('response', await response.text())
      if (!response.ok) {
        let errorBody: any;
        try {
          errorBody = await response.json();
        } catch {
          errorBody = await response.text();
        }
        return { success: false, error: errorBody };
      }

      // 👇 handle blob download or json based on responseType
      const isBlob = xheaders?.responseType === 'blob';
      const responseData = isBlob
        ? await response.blob()
        : await response.json();

      return { success: true, data: responseData };
    } catch (error: any) {
      return { success: false, error };
    }
  }

  async get(
    url: string,
    query?: string,
    headers?: HeaderType
  ): Promise<RequestResponse> {
    return this.request('GET', url, query, headers);
  }

  async post<T>(
    url: string,
    body: T,
    options?: HeaderType
  ): Promise<RequestResponse> {
    return await this.request('POST', url, body, options);
  }

  async put<T>(url: string, body: T): Promise<RequestResponse> {
    return this.request('PUT', url, body);
  }

  async patch<T>(url: string, body: T): Promise<RequestResponse> {
    return this.request('PATCH', url, body);
  }

  async delete(url: string): Promise<RequestResponse> {
    return this.request('DELETE', url);
  }
}

export default HTTPClient;

export function errorHandler(error: any) {
  if (error?.errors?.length > 0) {
    if (
      error?.errors[0].code === 401 && 
      window.location.pathname !== '/sign-in'
    ) {
      window.location.href = '/sign-in';
      return;
    }
    toast.error(error?.errors[0].message);
  } else {
    toast.error('Something went wrong. Please try again later.');
  }
}
