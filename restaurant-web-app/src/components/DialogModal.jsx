import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from './ui/dialog';
import { Button } from './ui/button';
import { cn } from '../lib/util';

// type Props = {
//   isOpen: boolean;
//   setIsOpen: (value: boolean) => void;
//   onSubmitFunction?: () => void;
//   onClose?: () => void;
//   onSubmitTitle?: string;
//   title?: string;
//   description?: string;
//   showActions?: boolean;
//   content: ReactNode;
//   size?: 'lg' | 'xl' | '2xl' | '3xl' | '4xl' | '5xl' | '6xl' | '7xl';
//   triggerComponent: ReactNode;
// };

const sizeMap = {
  lg: 'md:min-w-lg',
  xl: 'md:min-w-xl',
  '2xl': 'md:min-w-2xl',
  '3xl': 'md:min-w-3xl',
  '4xl': 'md:min-w-4xl',
  '5xl': 'md:min-w-5xl',
  '6xl': 'md:min-w-6xl',
  '7xl': 'md:min-w-7xl',
};

const DialogModal = ({
  isOpen,
  setIsOpen,
  onClose,
  onSubmitFunction,
  onSubmitTitle,
  title,
  description,
  showActions = true,
  content,
  triggerComponent,
  size = 'lg',
}) => {
  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen} className={'bg-white'}>
      <DialogTrigger asChild>{triggerComponent}</DialogTrigger>
      <DialogContent className={cn(sizeMap[size])}>
        <DialogHeader>
          {title && (
            <DialogTitle className="text-[#3D424F]">{title}</DialogTitle>
          )}
          {description && <DialogDescription>{description}</DialogDescription>}
        </DialogHeader>
        <div className="w-full">{content}</div>
        {showActions && (
          <DialogFooter>
            <Button
              variant="outline"
              onClick={() => {
                // eslint-disable-next-line @typescript-eslint/no-unused-expressions
                onClose && onClose();
                setIsOpen(false);
              }}
              className="cursor-pointer"
            >
              Cancel
            </Button>
            {onSubmitFunction && (
              <Button className="cursor-pointer" onClick={onSubmitFunction}>
                {onSubmitTitle}
              </Button>
            )}
          </DialogFooter>
        )}
      </DialogContent>
    </Dialog>
  );
};

export default DialogModal;
